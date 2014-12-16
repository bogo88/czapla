from django.db import models
from django.contrib.auth.models import Group, User

from meal.models import Restaurant


class Order(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(Group)
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    order_time = models.DateTimeField()

    def __unicode__(self):
        return self.name