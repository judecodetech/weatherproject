"""
Common models that will be shared between apps
"""
from django.db import models


class WeatherappModelBase(models.Model):
    """
    Base class providing default created and modified datetimes.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
