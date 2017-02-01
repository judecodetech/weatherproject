from django.conf.urls import include, url

from rest_framework import routers

from api import viewsets


router = routers.DefaultRouter()

router.register(r'weather_forecasts', viewsets.WeatherForecastViewSet, base_name='WeatherForecast')

urlpatterns = [ 
	url(r'^', include(router.urls)),
]