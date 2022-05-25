from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# import installed django country and phone field
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

TITLE_OPT = (("Mr", "Mr"), ("Mrs/Ms/Miss", "Mrs/Ms/Miss"), ("Dr", "Dr"))


class Profile(models.Model):
    """
    A profile model for maintaining default
    delivery information for users if save_info
    boolean is set to True in checkout_form.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_title = models.CharField(null=True, blank=True, choices=TITLE_OPT, max_length=20)
    default_first_name = models.CharField(max_length=50, null=True, blank=True)
    default_last_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = PhoneNumberField(null=True, blank=True, max_length=20)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


# receiver event (signal) to automatically add or 
# update profile when form is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
