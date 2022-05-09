from django.shortcuts import render
from reviews.models import Review


def index(request):
    """View to render index.html template"""

    context = {
        'reviews': Review.objects.filter(status=1).order_by('-created_on')
    }
    return render(request, 'home/index.html', context)
