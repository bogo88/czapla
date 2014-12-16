from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import Group

from order.models import Order


def index(request):
    if not request.user.is_authenticated():
        messages.warning(request, 'You have to be logged in to see groups')
        return redirect('profile:index')
    return render(request, 'group/index.html')


def details(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    orders = Order.objects.filter(group=group_id)
    if not request.user.is_authenticated():
        messages.warning(request, 'You have to be logged in to see groups')
        return redirect('profile:index')
    else:
        if not request.user.groups.filter(id=group_id).exists():
            messages.warning(request, 'You don\'t belong to this group')
            return redirect('group:index')
        else:
            return render(request, 'group/details.html', {'group':group, 'orders':orders.all()})