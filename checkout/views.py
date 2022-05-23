from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from .models import Order, OrderLineItem
from products.models import Product

from basket.contexts import basket_contents

import stripe
import json


@require_POST
def save_checkout_data(request):
    """
    Function to check if save_info fieldset is
    set to True or False - ticked/unticked 
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """X"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'title': request.POST['title'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'house_number': request.POST['house_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_city': request.POST['town_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'delivery_instructions': request.POST['delivery_instructions'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We're sorry, but there is an issue with a basket item"
                        f"No payment has been accepted for {order.order_number}"
                        "We will empty your basket, please try again!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_confirm', args=[order.order_number]))
        else:
            messages.error(request, 'There is an error with your form. \
                Please try again.')
    else:
        basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket, search our newest products!")
        return redirect(reverse('products'))

    # to get the current total of session bag for stripe payment
    current_basket = basket_contents(request)
    total = current_basket['order_total']
    # stripe requires amount to be charged as integer so *100
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                Please make sure it is set in your envrionment correctly.')

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_confirm(request, order_number):
    """
    To display final confirmation page with
    the order details and a customised message
    for each customer with successfull payment
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Thank you for your order {order.title}. \
        {order.last_name}! We are currently working on your order \
            {order_number}. An email will be sent shortly to {order.email}.')

    # deleting bag in session as it is no longer needed
    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_confirm.html', context)
