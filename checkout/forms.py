from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    """
    Generates the order form using the
    imported Order model. Defining fields
    to include and placeholders for specific
    fields.
    """
    class Meta:
        """
        Meta class to defind model used and fields
        to include
        """
        model = Order
        fields = ('title', 'first_name', 'last_name',
                  'email', 'phone_number', 'house_number',
                  'street_address1', 'street_address2',
                  'town_city', 'county', 'country', 'postcode'
              )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # dictionary of placeholders for order form
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'house_number': 'House No.',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country' and 'title':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
