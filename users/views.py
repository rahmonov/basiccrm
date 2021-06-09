from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from users.forms import CustomUserCreationForm


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
            return redirect(reverse('landing'))
        else:
            return render(request, template_name='users/register.html', context={'form': form})
