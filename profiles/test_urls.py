from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import profile, order_history


class TestProductUrls(SimpleTestCase):
    """
    Testing all profile urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_profile_url(self):
        """Testing profile/ url (function = url name)"""
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_order_history_url(self):
        """Testing profile/ order_history url (function = url name)"""
        url = reverse('order_history', args=['order_number'])
        self.assertEquals(resolve(url).func, order_history)
