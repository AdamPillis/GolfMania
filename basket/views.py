from django.shortcuts import render

def view_basket(request):
    """
    View to render basket.html template
    containing items added by user
    """

    return render(request, 'basket/basket.html')
