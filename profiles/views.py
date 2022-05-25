from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile
    """
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile_form': profile_form,
        'orders': orders,
    }
    return render(request, template, context)