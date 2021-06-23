from django.shortcuts import render
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'landing.html'
