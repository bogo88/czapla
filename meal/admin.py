from django.contrib import admin

from meal.models import Meal, Restaurant, Rating

admin.site.register(Meal)
admin.site.register(Restaurant)
admin.site.register(Rating)