#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.template import Context

from order.models import Order
from meal.models import Meal, Restaurant


def restaurant(request, group_id):
    if not request.user.is_authenticated():
        messages.warning(request, 'Musisz być zalogowany, żeby utworzyć zamówienie')
        return redirect('profile:index')
    else:
        if not request.user.groups.filter(id=group_id):
            messages.warning(request, 'Nie należysz do tej grupy')
            return redirect('profile:index')
        else:
            restaurants = Restaurant.objects.all()
            hours = range(1, 24)
            return render(request, 'meal/restaurant.html', {'restaurants': restaurants.all(),
                                                            'group_id': group_id,
                                                            'hours': hours,
                                                            })


def select(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    meals = Meal.objects.filter(restaurant=order.restaurant.id)
    if not request.user.groups.filter(id=order.group.id):
        messages.warning(request, 'To zamówienie nie należy do Twojej grupy')
        return redirect('profile:index')
    else:
        return render(request,'meal/select.html',{'meals': meals.all(),'order': order})