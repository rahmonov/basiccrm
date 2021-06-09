from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import CustomUserCreationForm


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
            form.save()
            return redirect(reverse('pages:home'))
        else:
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)

