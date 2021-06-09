from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User as CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {'username': UsernameField}
