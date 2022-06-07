from django.apps import AppConfig


class BasketConfig(AppConfig):
    """Configuring basket app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
