from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    """
    Inline admin class. Allows to add and edit
    lineitems in the admin inside the order model
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    setting fields automatically updated within model
    to uneditable
    """
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'sub_total',
                       'order_total', 'original_basket',
                       'stripe_pid')

    fields = ('order_number', 'date', 'title',
              'first_name', 'last_name', 'email',
              'house_number', 'phone_number', 'country',
              'postcode', 'town_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'sub_total', 'order_total', 'original_basket',
              'stripe_pid')

    list_display = ('order_number', 'date', 'last_name',
                    'sub_total', 'delivery_cost',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

# Register your models here.
