import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    appid = '25f3763955aaaf6059e58f006fb85083'  # этот ключ генерируется при регистрации на сервиче
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    # print(cities)

    all_cities = []

    for city in cities:
        # print(city)
        res = requests.get(url.format(city)).json()  # метод .json() представляет данные в виде словаря
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
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
    # Данные передаются через третий параметр функции render
