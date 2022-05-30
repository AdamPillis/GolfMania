from django import forms
from .widgets import CustomClearableFileInput
from .models import Category, Product


class ProductForm(forms.ModelForm):
    """
    Form created to add products
    """
    class Meta:
        """Selecting product as model and to include all fields"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
