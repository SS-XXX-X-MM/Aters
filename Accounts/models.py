from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=13, unique=True)
    is_active = models.BooleanField(_('active'), default=False, help_text=_('Designates whether this user should be treated as active.'))
    is_user = models.BooleanField(default=True)
    is_restaurant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Address(models.Model):
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length= 100, null=True, blank=True)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.city} - {self.pincode}'


    



    
