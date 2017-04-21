from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, RedirectView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from weatherapp.forms import RegistrationForm
from weatherapp.models import WeatherForecast
from weatherappauth.models import WeatherAppUser


class ForecastWeatherView(DetailView):
    template_name = 'weatherapp/weather_forecast.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        forecasts = WeatherForecast.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(forecasts, 3)
        try:
            forecast_list = paginator.page(page)
        except PageNotAnInteger:
            forecast_list = paginator.page(1)
        except EmptyPage:
            forecast_list = paginator.page(paginator.num_pages)

        context = {}
        context['weather_forecast_list'] = forecast_list

        return render(request, self.template_name, context)


class RegisterFormView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = '/register/success/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        new_user = WeatherAppUser.objects.create_user(
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password']
        )
        new_user.save()
        return super(RegisterFormView, self).form_valid(form)

class RegisterSuccessView(TemplateView):
    template_name = 'registration/success.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


