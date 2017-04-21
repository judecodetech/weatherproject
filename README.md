# Weather Project

## Django Weather Forecast

## To run this app, please follow the instructions below
		Open your terminal
		run git clone 
 		Navigate to root of project 'cd weatherproject'
** run the following commands in order:
source venv/bin/activate
Before you run the next command please make sure you have pip3
installed
otherwise install pip3 -- on Mac: brew install python3-pip, Linux: aptget
install python3-pip
pip3 install -r requirements.txt
pip3 install --upgrade pip -- just to make sure packages are up-to-date
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py crontab add -- Start Django management
command to collect weather forecasts
python3 manage.py crontab show -- To see the command that was
added.
This added command can be found in settings.py under CRONJOBS list
( Modify as suited )
python3 manage.py crontab remove -- To removce the cron command.
Please run this command if you do modify the CRONJOBS then re-run python3
manage.py crontab add
sudo python3 manage.py collectstatic -- I switched DEBUG off in
settings.py to turn off
debug messages.
So collectstatic command should
be run otherwise the
admin frontend will not
load static files. It is
all important to run
this command with
super user privileges for
complete write
access.
python3 manage.py runserver --insecure 127.0.0.1:8000 -- This starts 
the server in an insecure
 mode because DEBUG is off and it is
 not allowed to switch debug off in
 development mode. So the --insecure
 switch will bypass this for development mode.
 It is important that the server is run
 on the exact IP address(local host) in this
 command. If you want to run in a different
 IP address, please add the IP address in
 ALLOWED_HOSTS list in settings.py
All other processes will be performed on the frontend -- Navigation of the UI.
Well Except running:
python3 manage.py createsuperuser -- To enable you log on to
the admin backend
On first registration the there will be no weather data. To get instant data,
run the following command:
python3 manage.py weather_forecast

API
You must be a django user to view the API data otherwise you will be locked
out and thrown an error messsage.
After registering, to view the api data, vist the URL below:
http://127.0.0.1:8000/api/weather_forecasts/