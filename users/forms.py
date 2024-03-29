from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField

from users.models import User as CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {'username': UsernameField}


class CustomLoginForm(AuthenticationForm):
    pass
