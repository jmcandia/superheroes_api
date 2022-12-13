from django.contrib import admin

from .models import Superhero


class SuperheroAdmin(admin.ModelAdmin):
    list_display = ['name', 'alter_ego', 'year', 'editorial']


# Register your models here.
admin.site.register(Superhero, SuperheroAdmin)
