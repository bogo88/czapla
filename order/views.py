from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from order.models import Order
from item.models import Item
from meal.models import Restaurant




def details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = Item.objects.filter(order=order_id)
    if not request.user.is_authenticated():
        messages.warning(request, 'You have to be logged in to see orders')
        return redirect('profile:index')
    else:
        if not request.user.groups.filter(id=order.group.id).exists():
            messages.warning(request, 'This order don\'t belong to your group')
            return redirect('group:index')
        else:
            return render(request, 'order/details.html', {'order':order, 'items':items.all()})