from django.db import models
from django.utils import timezone

from tools.models import WeatherappModelBase
from weatherappauth.managers import WeatherAppUserManager


class WeatherForecast(WeatherappModelBase):
	"""
    Weather model.
    """
	date = models.CharField(max_length=50)
	max_temp = models.CharField(max_length=10, verbose_name='High Temperature')
	min_temp = models.CharField(max_length=10, verbose_name='Low Temperature')
	wind = models.CharField(max_length=10)
	rain = models.CharField(max_length=10)

	def __str__(self):
		return '{} --> high: {}, low: {}'.format(self.date, self.max_temp, self.min_temp)