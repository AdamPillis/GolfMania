from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    Renders product_detail.html to display
    all info regarding each specific product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
