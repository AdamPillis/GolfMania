from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import view_basket, add_to_basket, adjust_basket, remove_basket_item


class TestBasketUrls(SimpleTestCase):
    """
    Testing all basket urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_view_basket_url(self):
        """Testing basket/ url (function = url name)"""
        url = reverse('view_basket')
        self.assertEquals(resolve(url).func, view_basket)

    def test_add_to_basket_url(self):
        """Testing basket/ add_to_basket url (function = url name)"""
        url = reverse('add_to_basket', args=['item_id'])
        self.assertEquals(resolve(url).func, add_to_basket)

    def test_adjust_basket_url(self):
        """Testing basket/ adjust_basket url (function = url name)"""
        url = reverse('adjust_basket', args=['item_id'])
        self.assertEquals(resolve(url).func, adjust_basket)

    def test_remove_basket_item_url(self):
        """Testing basket/ remove_basket_item url (function = url name)"""
        url = reverse('remove_basket_item', args=['item_id'])
        self.assertEquals(resolve(url).func, remove_basket_item)
