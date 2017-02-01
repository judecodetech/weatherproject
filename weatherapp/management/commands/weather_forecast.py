from datetime import datetime
import json
from optparse import make_option
import re

from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import requests

from weatherapp.models import WeatherForecast

 
# Class MUST be named 'Command'
class Command(BaseCommand):
 
    # Displayed from 'manage.py help mycommand'
    help = "Get weather data"
 
    def handle(self, *app_labels, **options):
        """
        app_labels - app labels (eg. myapp in "manage.py reset myapp")
        options - configurable command line options
        """
 
        # Return a success message to display to the user on success
        # or raise a CommandError as a failure condition
            
        request_post = None
        url = 'http://weather.news24.com/sa/cape-town'
        city = 'cape town'

        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.content, 'html.parser')
        city_list = soup.find(id="ctl00_WeatherContentHolder_ddlCity")
        city_as_on_website = city_list.find(text=re.compile(city, re.I)).parent
        cityId = city_as_on_website['value']
        json_url = "http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx"

        headers = {
            'Content-Type': 'text/plain; charset=UTF-8',
            'Host': 'weather.news24.com',
            'Origin': 'http://weather.news24.com',
            'Referer': url,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
            'X-AjaxPro-Method': 'GetCurrentOne'
        }

        payload = {
            "cityId": cityId
        }

        request_post = requests.post(json_url, headers=headers, data=json.dumps(payload))
        data = request_post.text
        pattern = r"new Date\(Date\.UTC\((\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)\)\)"
        data = re.sub(pattern, convert_date, data)
        data = data.strip(";/*")
        data = json.loads(data)

        weather_forecast = WeatherForecast()

        # date value returned from api is one month behind
        weather_forecast.date = data['Forecast']['Date']
        weather_forecast.max_temp = data['Forecast']['HighTemp']
        weather_forecast.min_temp = data['Forecast']['LowTemp']
        weather_forecast.rain = data['Forecast']['PrecipitationProbability']

        # comparing the values from the api, the windspeed
        # value from obversations is the accurate one as
        # it is the same value to the one on the webiste
        # http://weather.news24.com/sa/cape-town
        for observation in data['Observations']:
            for key, value in observation.items():
                if city.title() == value:
                    weather_forecast.wind  = observation['WindSpeed']

        weather_forecast.save()

        return('Weather forecast data successfully collected')

def convert_date(match):
    return '"' + datetime(*map(int, match.groups())).strftime("%Y-%m-%dT%H:%M:%S") + '"'

 
