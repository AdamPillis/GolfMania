from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Form to render profile of user
    requesting in profile.html
    """
    class Meta:
        """
        Profile model to use and
        exclude user
        """
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_phone_number': 'Phone Number',
            'default_house_number': 'House Number',
            'default_postcode': 'Postal Code',
            'default_town_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country' and field != 'default_title':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black'
            self.fields[field].label = False
