from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CheckoutForm


def checkout(request):
    """X"""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
    }

    return render(request, template, context)
