from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    To give the admin the ability to filter and search for
    specific profiles
    """
    list_display = ('default_last_name', 'default_first_name')
    list_filter = (
        'default_town_city', 'default_last_name',
        'default_phone_number', 'default_country', 'default_postcode'
        )
    search_fields = ['default_last_name']
