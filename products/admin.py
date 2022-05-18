from django.contrib import admin
from .models import Product, Category, Brand


class ProductAdmin(admin.ModelAdmin):
    """To customise products view via admin panel"""
    list_display = (
        'brand',
        'hand_type',
        'type',
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class BrandAdmin(admin.ModelAdmin):
    """To customise brand view via admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    """To customise cateogry view via admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
