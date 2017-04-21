# Weather Project

## Django Weather Forecast

### To run this app, please follow the instructions below

Open your terminal
Before you run the next command please make sure you have pip3 is installed
To install pip3:
    on Mac: brew install python3-pip, Ubuntu: aptget install python3-pip

run **pip3 install -e git+https://github.com/judeconnectionz/weatherproject.git@master#egg=weatherproject**

Please make sure the above command is run with root privilege

The above command will pull in the weather project into a new folder called **src**
And please change the owner of the **src** file using the command below so that you will
be allowed to run the pip3 command without **sudo**
**chown -R your_user:your_user src

Navigate to root of project **cd src/weatherproject**

**virtualenv -p python3 venv**
**source venv/bin/activate**
**which python3** - This command should output the **/src/weatherproject** as the beginning of its output

**pip3 install -r requirements.txt**

**pip3 install --upgrade pip** -- just to make sure packages are up-to-date
**python3 manage.py makemigrations**
**python3 manage.py migrate**

**python3 manage.py crontab add** -- Start Django management command to collect weather forecasts
**python3 manage.py crontab show** -- To see the command that was added.
This added command can be found in settings.py under CRONJOBS list ( Modify as suited )
**python3 manage.py crontab remove** -- To removce the cron command.
**Please run this command if you do modify the CRONJOBS **python3 manage.py crontab add**

**python3 manage.py collectstatic** -- I switched DEBUG off in settings.py to turn off debug messages. So collectstatic command should be run otherwise the admin frontend will not load static files. It is also important to run this command with super user privileges for complete write access.

**python3 manage.py runserver --insecure 127.0.0.1:8000** -- This starts the server in an insecure mode because DEBUG is off as it is not allowed to switch debug off in development mode. So the --insecure switch will bypass this for development mode. It is important that the server is run on the exact IP address(local host) in this command. If you want to run it with different IP address, please add the IP address in ALLOWED_HOSTS list in **weatherproject/weatherapp/settings.py**

Once the above have been successful, navigate to your browser and enter the following address:
	**http://127.0.0.1:8000** -- You should see a login page.

All other processes will be performed on the frontend -- Navigation of the UI.
Well Except running:
	**python3 manage.py createsuperuser** -- To enable you log on to the admin backend
	The above command will prompt you for an email and password, which will enable you
	logon to view weather data.
	
	On first registration there will be no weather data. To get instant data,
	run the following command:
		**python3 manage.py weather_forecast**

## API
You must be a django user to view the API data otherwise you will not be granted access.
	After registering, to view the api data, vist the URL below:
		**http://127.0.0.1:8000/api/weather_forecasts/**


## Use the following command to run the tests:
**python3 manage.py test**
