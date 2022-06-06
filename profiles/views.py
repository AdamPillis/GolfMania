from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """
    Display the user's profile
    """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

    profile_form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile_form': profile_form,
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, template, context)


def order_history(request, order_number):
    """
    Function to get all orders linked with request.user
    and display each within the table of profile.html
    through context
    """
    order = get_object_or_404(Order, order_number=order_number)
    products = Product.objects.all()

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        f'A confirmation email was sent on the {order.date} to {order.email}'
    ))

    template = 'checkout/checkout_confirm.html'
    context = {
        'order': order,
        'products': products,
        # to check if user is coming from profile page
        'from_profile_page': True,
    }

    return render(request, template, context)
