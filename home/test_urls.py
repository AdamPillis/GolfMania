from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import index, error_404, error_500


class TestHomeUrls(SimpleTestCase):
    """
    Testing all urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_home_view_url(self):
        """Testing home/ url (function = url name)"""
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
