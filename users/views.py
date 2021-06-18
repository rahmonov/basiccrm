from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, BusinessOwner
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout


class UserSignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()

        context = {
            'form': form
        }

        return render(request=request, template_name='users/signup.html', context=context)

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            # creating new business owner when there is new user singing up
            BusinessOwner.objects.create(user=user)
            return redirect(reverse('users:login'))

        else:
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()

        context = {
            'form': form
        }

        return render(request, 'users/signin.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = get_object_or_404(User, username=form.cleaned_data['username'])
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('clients:index')

        context = {
            'form': form
        }
        return render(request, 'users/signin.html', context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out")
        return redirect('pages:home')