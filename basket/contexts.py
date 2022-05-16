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

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
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
