from django.test import TestCase

from weatherapp.tests import WeatherAppUserTestCase
from weatherappauth import models



class WeatherAppModelTests(WeatherAppUserTestCase):
    """
    Tests for WeatherAppUser and its custom manager.
    
    """
    def test_anonymous_user_is_inactive(self):
        """
        Test that a Anonymous user is inactive.
        
        """
        self.failIf(self.anonymous_user.is_active)
        

    def test_new_user_is_active(self):
        """
        Test that a newly-created user is active.
        
        """
        self.failUnless(models.WeatherAppUser.objects.get(pk=self.sample_user.pk).is_active)
