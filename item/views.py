from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from order.models import Order
from item.models import Item
from item.models import Meal


def add(request, order_id, meal_id):
    order = get_object_or_404(Order, pk=order_id)
    meal = get_object_or_404(Meal, pk=meal_id)
    user = get_object_or_404(User, pk=request.user.id)
    item = Item()
    if not request.user.groups.filter(id=order.group.id):
        messages.warning(request, 'This order don\'t belong to your group')
        return redirect('group:index')
    else:
        item.order = order
        item.meal = meal
        item.user = user
        item.save()
        messages.success(request, 'Meal added to list')
        return HttpResponseRedirect(reverse('order:details', args=[order.id]))