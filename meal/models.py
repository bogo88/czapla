from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    meal = models.ForeignKey(Meal)
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(User)
    value = models.IntegerField()
    comment = models.CharField(max_length=500)

    def stars(self):
        return range(0,self.value)