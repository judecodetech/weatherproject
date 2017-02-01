from django.conf.urls import include, url

from weatherapp import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', views.log_user_out, name='logout'),

    # If user is not logged in, it will redirect to login page
    url(r'^accounts/login/$', auth_view.login),

    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='successful_registration'),
    url(r'^weather_forecast/$', views.forecast_weather, name='weather_forecast'),
]
