from django.db import models

TYPE_STATUS = (
    ("New", "New"),
    ("Used", "Used")
    )


class Brand(models.Model):
    """
    Class to list all golf brands available
    on the site which will link to all products
    via foreign key
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """returns category name as string"""
        return self.name

    def get_friendly_name(self):
        """returns friendly name of category"""
        return self.friendly_name


class Category(models.Model):
    """
    Class to categorise GolfMania's products
    name used in developement like search/filter functionality
    friendly_name is visual to the user instead of the name
    """
    class Meta:
        """To fix plural issue relating to django"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """returns category name as string"""
        return self.name

    def get_friendly_name(self):
        """returns friendly name of category"""
        return self.friendly_name


class Product(models.Model):
    """
    Model for every product hosted on Golf Mania
    Each need to include essential data such as name, description,
    category type, price and rest is optional.
    """
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    type = models.CharField(
    choices=TYPE_STATUS, default=False, max_length=20
    )
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_quality = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """X"""
        return self.name
