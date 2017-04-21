from django.conf.urls import include, url
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

from weatherapp import views
from weatherapp.views import(
	ForecastWeatherView, LogoutView, 
	RegisterFormView, RegisterSuccessView
)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='weatherapp/homepage.html'), name='homepage'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # If user is not logged in, it will redirect to login page
    url(r'^accounts/login/$', auth_view.login),

    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^register/success/$', RegisterSuccessView.as_view(), name='successful_registration'),
    url(r'^weather_forecast/$', ForecastWeatherView.as_view(), name='weather_forecast'),
]
