from django.test import SimpleTestCase
from .forms import ProfileForm


class TestForms(SimpleTestCase):
    """
    Testing ProfileForm
    """
    databases = '__all__'

    def test_profile_form_no_data(self):
        """
        testing if profile form has any errors.
        The result should be 0 given that the 
        user can fill in any field within
        profile.html without an error showing.
        The delivery form is the one with required
        fields
        """
        form = ProfileForm(data={})

        self.assertEquals(len(form.errors), 0)