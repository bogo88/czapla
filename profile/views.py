#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError

from home.forms import LoginForm, RegisterForm


def index(request):
    form = LoginForm()
    if request.POST:
        try:
            log_out = request.POST['logout']
        except MultiValueDictKeyError:
            log_out = False
        if log_out:
            logout(request)
            messages.success(request, 'Wylogowano')
            return redirect('home:index')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Witaj '+username)
                return redirect('home:index')
            else:
                messages.warning(request, 'Twoje konto nie jest aktywne')
        else:
            messages.warning(request, 'Błędna nazwa użytkownika lub hasło')
    return render(request, 'profile/index.html', {'form': form})


def register(request):
    form = RegisterForm(request.POST)
    if request.POST:
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            messages.success(request, u'Witaj %s, dziękujemy za utworzenie konta.' % (request.POST['username']))
            return redirect('home:index')
        else:
            for err in form.errors:
                messages.warning(request, form.errors[err])
    return render(request, 'profile/register.html', {'form': form})