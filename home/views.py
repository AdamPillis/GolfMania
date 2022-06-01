from django.shortcuts import render
from reviews.models import Review
from products.models import Product


def index(request):
    """View to render index.html template"""
    products = Product.objects.all()

    context = {
        'products': products,
        'reviews': Review.objects.filter(status=1).order_by('-created_on')
    }
    return render(request, 'home/index.html', context)
