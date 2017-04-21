from distutils.core import setup

setup(
    name='weatherproject',
    version='0.1',
    packages=['weatherproject',],
    author = "Jude Ugbefu",
    author_email = "judeconnectionz@gmail.com",
    description = ("This project collects weather data from weather.news24 "
                        "and displays this data to a user."),
    license='None',
    long_description=open('README.md').read(),
)