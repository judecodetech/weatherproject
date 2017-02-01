from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from weatherapp.forms import RegistrationForm
from weatherapp.models import WeatherForecast
from weatherappauth.models import WeatherAppUser


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = WeatherAppUser.objects.create_user(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            new_user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
     
def register_success(request):
    return render(request, 'registration/success.html')
 
def log_user_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def homepage(request):
    return render(request, 'weatherapp/homepage.html', {})

@login_required
def forecast_weather(request):
    forecasts = WeatherForecast.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(forecasts, 3)
    try:
        forecast_list = paginator.page(page)
    except PageNotAnInteger:
        forecast_list = paginator.page(1)
    except EmptyPage:
        forecast_list = paginator.page(paginator.num_pages)

    return render(request, 'weatherapp/weather_forecast.html', {'weather_forecast_list': forecast_list})
