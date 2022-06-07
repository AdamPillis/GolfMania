from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    all_products, add_product, update_product, delete_product)


class TestProductUrls(SimpleTestCase):
    """
    Testing all products urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_product_url(self):
        """Testing products/ products url (function = url name)"""
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_add_product_url(self):
        """Testing products/ add_product url (function = url name)"""
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)

    def test_update_product_url(self):
        """Testing products/ update_product url (function = url name)"""
        url = reverse('update_product', args=['product-id'])
        self.assertEquals(resolve(url).func, update_product)

    def test_delete_product_url(self):
        """Testing products/ delete_product url (function = url name)"""
        url = reverse('delete_product', args=['product-id'])
        self.assertEquals(resolve(url).func, delete_product)
