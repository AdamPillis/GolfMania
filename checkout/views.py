from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """X"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
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
