"""
used to generate the order number
"""
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# import installed django countries field
from django_countries.fields import CountryField

from products.models import Product
# attaching profile model once profile app created

TITLE_OPT = (("Mr", "Mr"), ("Mrs/Ms/Miss", "Mrs/Ms/Miss"), ("Dr", "Dr"))


class Order(models.Model):
    """
    Order Model containing all personal user information
    required to buy products online. Also includes order
    details and total charges
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # setting on delete to null if the profile is deleted so order history 
    # remains in admin and allow users to make purchases without profile
    title = models.CharField(
        choices=TITLE_OPT, default=False, max_length=20
        )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = PhoneNumberField()
    house_number = models.IntegerField(null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    delivery_instructions = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    # private method to this class only
    def _generate_order_number(self):
        """
        _ ensures this is a private function and only
        used in this class. Generates a random, unique
        order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item
        is added, accounting for delivery costs.
        """
        self.sub_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0  # if all line items are deleted, set to 0 so no error if order total is zero
        if self.sub_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_CHARGE
        else:
            self.delivery_cost = 0
        self.order_total = self.sub_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the
        order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save()

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Used for each item by iterating through bag items
    and attaching the following to each of the items
    and update delivery_cost, order_total and 
    grand_total along the way
    """
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the
        order number if it hasn't been set already.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

