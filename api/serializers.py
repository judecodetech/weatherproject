from rest_framework import serializers

from weatherapp import models


class WeatherForecastSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = models.WeatherForecast