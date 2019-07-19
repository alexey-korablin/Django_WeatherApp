import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    appid = '25f3763955aaaf6059e58f006fb85083'  # этот ключ генерируется при регистрации на сервиче
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Ryazan'
    res = requests.get(url.format(city)).json()  # метод .json() представляет данные в виде словаря

    print(res)

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    print(city_info)

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)    # возвращает результат вызова функции render, одним из
    # параметров которой является шаблон. Не указываем папку templates, потому что поиск по умолчанию ведется там.
    # Данные передаются через третий параметр функции render
