"""
Custom auth models for the Weather App.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from weatherappauth.managers import WeatherAppUserManager

from tools.models import WeatherappModelBase


class WeatherAppUser(AbstractBaseUser, WeatherappModelBase, PermissionsMixin):
    """
    Custom user model to allow email to map to username field.
    """
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = WeatherAppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email
        return self.email

    def get_short_name(self):
        # The user is identified by their email
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
