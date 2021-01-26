from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class CustomUser(AbstractUser):
    display_name = models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
    address1 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
    address2 = models.CharField(verbose_name=_("Address line 2"), max_length=1024, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_("Postal Code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True, null=True)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to='photos/', default='photos/ereader.png')

    class Meta:
        ordering = ['username']

    def get_absolute_url(self):
        return reverse('account_profile')

    def __str__(self):
        return f"{self.username}"

   
