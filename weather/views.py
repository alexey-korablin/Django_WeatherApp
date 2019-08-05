import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm
from .utils import weather_utils

# Create your views here.


def index(request):
    appid = '25f3763955aaaf6059e58f006fb85083'  # этот ключ генерируется при регистрации на сервисе. Нужен для
                                                # выполнения запросов к API
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid  # {} - скобки в адресе
    # служат для подстановки параметров, в данному случае названия города

    if request.method == 'POST':
        form = CityForm(request.POST)
        print(form)
        print(CityForm)
        form.save()

    form = CityForm()

    cities = City.objects.all() # взять все объекты из таблицы City
    # print(cities)

    all_cities = []

    for city in cities:
        # print(city)
        res = requests.get(url.format(city)).json()  # метод .json() представляет данные в виде словаря
        # print(res)
        # print(weather_utils.wind_direction(res))
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'pressure': res['main']['pressure'],
            'humidity': res['main']['humidity'],
            'wind': weather_utils.wind_direction(res),
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    # print(all_cities)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)    # возвращает результат вызова функции render, одним из
    # параметров которой является шаблон. Не указываем папку templates, потому что поиск по умолчанию ведется там.
    # Данные передаются через третий параметр функции render - context
