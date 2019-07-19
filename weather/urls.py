
from django.urls import path
from . import views  # подключаем файл views из корневой директории

urlpatterns = [
    path('', views.index)  # файл views содержит функцию index (пишем сами)
]