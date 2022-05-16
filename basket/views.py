from django.shortcuts import render, redirect


def view_basket(request):
    """
    View to render basket.html template
    containing items added by user
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ 
    Add a quantity of a specific type of product
    to the shopping basket
    """
    # converting string request data to integer
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # create var for basket if doesn't already exist
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
