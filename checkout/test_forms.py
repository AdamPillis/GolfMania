from django.test import SimpleTestCase
from .forms import CheckoutForm


class TestForms(SimpleTestCase):
    """
    Testing CheckoutForm
    """
    databases = '__all__'

    def test_checkout_form_no_data(self):
        """
        testing if Checkout form has any errors.
        The result is 7 because the title has a
        set default and the others are shown with
        a '*'.
        """
        form = CheckoutForm(data={})

        self.assertEquals(len(form.errors), 7)
