from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def basket_contents(request):
    """X"""
    basket_items = []
    total = 0
    product_count = 0
    # storing session's basket in var
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        # checking to see if item only has quality data
        # only quality is an integer so everything else
        # chosen by customer is a string i.e size, hand..
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_difference = 0

    order_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'order_total': order_total,
    }

    return context
