from django.shortcuts import render


def index(request):
    """View to render index.html template"""

    return render(request, 'home/index.html')
