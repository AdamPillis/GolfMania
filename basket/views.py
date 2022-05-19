from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from products.models import Product


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
    # using product var to display detailed toasts
    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request, f"Updated: Size '{size.upper()}' {product.name} quantity to {basket[item_id]['items_by_size'][size]}")
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added Size "{size.upper()}" {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added: Size "{size.upper()}" {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f"Updated: Quantity of {product.name} to '{basket[item_id]}'")
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {quantity} x {product.name} to your basket.')

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of a specified product
    within the basket.
    """
    # product stored in variable in order to be used
    # for messaging
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f"Updated: Size '{size.upper()}' {product.name} quantity to {basket[item_id]['items_by_size'][size]}")
        else:
            del basket[item_id]['items_by_size'][size]
            # if item id/size is not in bag, remove
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f"Removed: Size '{size.upper()}' {product.name} from your basket")
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f"Updated: {product.name} quantity to '{basket[item_id]}'")
        else:
            basket.pop(item_id)
            messages.success(request, f"Removed: '{product.name}'' from your basket")

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_basket_item(request, item_id):
    """
    Remove a specific item from the shopping
    basket, depending on size.
    """
    # product stored in variable in order to be used
    # for messaging
    product = get_object_or_404(Product, pk=item_id)
    # using a try block to catch any exceptions and
    # if so, return a status 500 page.
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f"Removed: Size '{size.upper()}' {product.name} from your basket")
        else:
            basket.pop(item_id)
            messages.success(request, f"Removed: '{product.name}' from your basket")

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)