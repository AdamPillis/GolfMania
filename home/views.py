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


def error_404(request, exception):
    """Renders custom 404.html when error code is 404"""
    return render(request, '404.html')


def error_500(request):
    """Renders custom 500.html when error code is 500"""
    return render(request, '500.html')