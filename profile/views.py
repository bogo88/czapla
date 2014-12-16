from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError

from home.forms import LoginForm


def index(request):
    form = LoginForm()
    if request.POST:
        try:
            log_out = request.POST['logout']
        except MultiValueDictKeyError:
            log_out = False
        if log_out:
            logout(request)
            messages.success(request, 'Logged out')
            return redirect('home:index')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Welcome '+username)
                return redirect('home:index')
            else:
                messages.warning(request, 'Your account is disabled')
        else:
            messages.warning(request, 'Wrong username or password')
    return render(request, 'profile/index.html', {'form': form})