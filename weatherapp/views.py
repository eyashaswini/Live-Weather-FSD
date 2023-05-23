import requests
import datetime
from django.shortcuts import render


# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mthatha'

    APPID = '9c73efbf0f561fccd3e8c3e8d0cdbe19'
    URL = 'https://api.openweathermap.org/data/2.5/weather?'
    PARAMS = {'q': city, 'appid': APPID, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    visibility = res['visibility']

    day = datetime.date.today()


    return render(request, 'weatherapp/index.html', {'description': description,
                                                     'icon': icon, 'temp': temp,
                                                     'day': day, 'city': city,
                                                     'pressure' : pressure,
                                                     'humidity': humidity,
                                                     'visibility': visibility})