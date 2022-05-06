from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


# In admin panel, review application settings are set here
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    summernote django app installed and
    replaces content sections for user input.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'likes', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
