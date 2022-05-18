from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Function to return basket items subtotal
    by multiplying price by quantity
    """
    return price * quantity
