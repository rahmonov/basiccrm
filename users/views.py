from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from users.forms import CustomUserCreationForm
from users.models import User


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()

        context = {
            'form': form
        }

        return render(request, template_name='users/register.html', context=context)

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('landing')
        else:
            return render(request, template_name='users/register.html', context={'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }

        return render(request, template_name='users/login.html', context=context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('clients:list')

        return render(request, template_name='users/login.html', context={'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out")
        return redirect('landing')
