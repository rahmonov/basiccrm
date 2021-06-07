from django.shortcuts import render


def landing(request):
    return render(request, template_name='landing.html')
