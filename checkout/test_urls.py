from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import save_checkout_data, checkout, checkout_confirm
from .webhooks import webhook


class TestCheckoutUrls(SimpleTestCase):
    """
    Testing all checkout urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_checkout_url(self):
        """Testing checkout/ checkout url (function = url name)"""
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_confirm_url(self):
        """Testing checkout/ checkout_confirm url (function = url name)"""
        url = reverse('checkout_confirm', args=['order_number'])
        self.assertEquals(resolve(url).func, checkout_confirm)

    def test_save_checkout_data_url(self):
        """Testing checkout/ save_checkout_data url (function = url name)"""
        url = reverse('save_checkout_data')
        self.assertEquals(resolve(url).func, save_checkout_data)

    def test_webhook_url(self):
        """Testing checkout/ webhook url (function = url name)"""
        url = reverse('webhook')
        self.assertEquals(resolve(url).func, webhook)
