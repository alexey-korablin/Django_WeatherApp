
from django.urls import path
from . import views  # подключаем файл views из текущей директории

urlpatterns = [
    path('', views.index)  # файл views содержит функцию index (пишем сами). Функция index возвращает результат
]                          # выполнения функции render. render принимает 3 аргумента: request (объект запроса),
                           # строку - путь к шаблону, который нужно отобразить и context (объект с данными,
                           # используемыми в шаблоне)