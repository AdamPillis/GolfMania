from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Renders products.html and displays
    all products on website. Search and 
    filter option will also be included.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
