from django.test import SimpleTestCase
from .forms import ProductForm


class TestForms(SimpleTestCase):
    """
    Testing product form
    """
    databases = '__all__'

    def test_product_form_no_data(self):
        """
        testing if product form was submitted blank, number
        of error would equal to 5 (5 fields required)
        """
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
