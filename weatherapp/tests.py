from django.contrib.auth.models import AnonymousUser
from django.core.management import call_command
from django.test import Client, TestCase, RequestFactory
from django.utils.six import StringIO

from weatherapp import forms, views
from weatherappauth import models


class WeatherAppUserTestCase(TestCase):
    """
    Base class for the test cases; -- 
    which is used to exercise various parts of
    the application.
    
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.sample_user = models.WeatherAppUser.objects.create_user(
            email='foo@bar.com', password='top_secret')
        self.anonymous_user = AnonymousUser()


class WeatherAppTests(WeatherAppUserTestCase, TestCase):

    def test_homepage(self):
        """
        Test that the homepage URL works
        without a user logging in.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_register(self):
        """
        Test that the weather forecast URL does not
        return a 200 success code without being accessed
        by a logged in user
        """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)


    def test_weather_forecast(self):
        """
        Test that the weather forecast URL does not
        return a 200 success code without being accessed
        by a logged in user
        """
        response = self.client.get('/weather_forecast/')
        self.assertNotEqual(response.status_code, 200)


    def test_command_output(self):
        out = StringIO()
        call_command('weather_forecast', stdout=out)
        self.assertIn('Weather forecast data successfully collected', out.getvalue())


    def test_registered_user_visit_view_weather_forecast(self):
        # Create an instance of a GET request to /weather_forecast/
        # using a registered user.
        request = self.factory.get('/weather_forecast/')
        request.user = self.sample_user
        response = views.forecast_weather(request)
        self.assertEqual(response.status_code, 200)


    def test_anonymous_user_visit_view_weather_forecast(self):
        # Create an instance of a GET request to /weather_forecast/
        # using an anonymous user.
        request = self.factory.get('/weather_forecast/')
        request.user = AnonymousUser()
        response = views.forecast_weather(request)
        self.assertNotEqual(response.status_code, 200)


class RegistrationFormTests(WeatherAppUserTestCase):
    """
    Tests for the forms and custom validation logic.
    
    """
    def test_registration_form(self):
        """
        Test that ``RegistrationForm`` enforces email constraints
        and matching passwords.
        
        """
        invalid_data_dicts = [
            # Incorrect email.
            {
            'data':
            { 'email': 'fooexample.com',
              'password': 'foo',
              'password_repeat': 'foo' },
            'error':
            ('email', [u"Enter a valid email address."])
            },
            # Mismatched passwords.
            {
            'data':
            { 'email': 'foo@example.com',
              'password': 'foo',
              'password_repeat': 'bar' },
            'error':
            ('__all__', [u"Passwords don't match"])
            },
            ]

        for invalid_dict in invalid_data_dicts:
            form = forms.RegistrationForm(data=invalid_dict['data'])
            self.failIf(form.is_valid())
            self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

        form = forms.RegistrationForm(data={ 'email': 'foo@example.com',
                                             'password': 'foo',
                                             'password_repeat': 'foo' })
        self.failUnless(form.is_valid())


    def test_registration_form_unique_email(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.
        
        """
        existing_data_dict = [
            # Already-existing email.
            {
            'data':
            { 'email': 'foo@bar.com',
              'password': 'secret',
              'password_repeat': 'secret' },
            'error':
            ('email', [u"The email already exists. Please try another one."])
            },
        ]

        for existing_data in existing_data_dict:
            form = forms.RegistrationForm(data=existing_data['data'])
            self.failIf(form.is_valid())
            self.assertEqual(form.errors[existing_data['error'][0]], existing_data['error'][1])

        form = forms.RegistrationForm(data={ 'email': 'foo@example.com',
                                                        'password': 'foo',
                                                        'password_repeat': 'foo' })
        self.failUnless(form.is_valid())
