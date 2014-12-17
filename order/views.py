#-*- coding: utf-8 -*-
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import Group

from order.models import Order
from item.models import Item
from meal.models import Restaurant


def details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = Item.objects.filter(order=order_id)
    if not request.user.is_authenticated():
        messages.warning(request, 'Musisz być zalogowany, żeby zobaczyć zamówienia')
        return redirect('profile:index')
    else:
        if not request.user.groups.filter(id=order.group.id).exists():
            messages.warning(request, 'To zamówienie nie należy do Twojej grupy')
            return redirect('profile:index')
        else:
            return render(request, 'order/details.html', {'order': order, 'items': items.all()})


def add(request):
    model = Order()
    if request.POST:
        group = get_object_or_404(Group, pk=request.POST.get('group'))
        restaurant = get_object_or_404(Restaurant, pk=request.POST.get('restaurant'))
        time = request.POST.get('hours')+':'+request.POST.get('minutes')
        order_date = datetime.datetime.strptime(request.POST.get('date')+' '+time, '%d-%m-%Y %H:%M')
        model.name = request.POST.get('name')
        model.user = request.user
        model.group = group
        model.restaurant = restaurant
        model.order_time = order_date
        model.save()
        messages.success(request, 'Order created')
        return redirect('order:details', model.id)