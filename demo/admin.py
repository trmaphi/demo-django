from django.contrib import admin
from .models import People, Planet

# Decorators to register these models inside admin page


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass
