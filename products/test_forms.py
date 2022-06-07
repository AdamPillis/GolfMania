from django.test import SimpleTestCase
from .forms import ProductForm


class TestForms(SimpleTestCase):
    """
    Testing product form
    """
    databases = '__all__'

    def test_product_form_no_data(self):
        """
        testing if form was submitted blank, number
        of error would equal to 4 (4 fields required)
        """
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)