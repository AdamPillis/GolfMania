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

    # setting size to none and checking if size is requested
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # setting quality to none and checking if requested
    quality = None
    if 'product_quality' in request.POST:
        quality = request.POST['product_quality']

    # create var for basket if doesn't already exist
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                # messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                # messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            # messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity


    request.session['basket'] = basket

    return redirect(redirect_url)
