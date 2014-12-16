from django.db import models
from django.contrib.auth.models import User

from order.models import Order
from meal.models import Meal


class Item(models.Model):
    meal = models.ForeignKey(Meal)
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order)

    def __unicode__(self):
        return self.meal.name