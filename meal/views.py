from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from order.models import Order
from meal.models import Meal, Restaurant


def restaurant(request):
    if not request.user.is_authenticated():
        messages.warning(request, 'You have to be logged in to create order')
        return redirect('profile:index')
    else:
        restaurants = Restaurant.objects.all()
        return render(request, 'meal/restaurant.html', {'restaurants': restaurants.all()})


def select(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    meals = Meal.objects.filter(restaurant=order.restaurant.id)
    if not request.user.groups.filter(id=order.group.id):
        messages.warning(request, 'This order don\'t belong to your group')
        return redirect('group:index')
    else:
        return render(request,'meal/select.html',{'meals': meals.all(),'order': order})