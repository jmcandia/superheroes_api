from django.contrib import admin
from django.urls import path

from .views import superhero_detail, superheroes_list

urlpatterns = [
    path('superheroes/', superheroes_list),
    path('superheroes/<int:id>/', superhero_detail),
]
