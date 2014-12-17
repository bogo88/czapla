#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm


class MealForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'NAzwa',
                                                         'required': 'required'}),
                           max_length=100,
                           required=True)
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Cena',
                                                             'required': 'required'}),
                               required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Opis'}),
                                  max_length=500)


class RateForm(forms.Form):
    value = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Nazwa użytkownika',
                                                             'required': 'required'}),
                               label="")
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Hasło',
                                                                 'required': 'required'}),
                               label="")


class RegisterForm(UserCreationForm):
    username = forms.RegexField(max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and "
                                "@/./+/-/_ only.",
                                error_messages={
                                'invalid': "This value may contain only letters, numbers and "
                                "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Nazwa użytkownika',
                                                              'required': 'required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Hasło',
                                                                  'required': 'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Powtórz hasło',
                                                                  'required': 'required'}),
                                help_text="Powtórz hasło")
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Imię'}),
                                 required=False)
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Nazwisko'}),
                                required=False)

