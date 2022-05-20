from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """X"""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    # to get the current total of session bag for stripe payment
    current_basket = basket_contents(request)
    total = current_basket['order_total']
    # stripe requires amount to be charged as integer so *100
    stripe_total = round(total * 100)

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51KngroIqDjTO0Fk0DppXT5thZtF0JaI0gfxwhTE2wd13JzvfIi4pFNYrJf3JB8bMwtaszxEN6uJoeYgwehbdrUJi00BkNkfTkn',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
