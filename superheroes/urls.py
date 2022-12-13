from django.contrib import admin
from django.urls import path

from .views import superheroes_list

urlpatterns = [
    path('superheroes/', superheroes_list),
    path('superheroes/<int:id>', superheroes_list),
]
