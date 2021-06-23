from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from clients.models import Client


class LandingView(TemplateView):
    template_name = 'landing.html'


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        total_client_count = Client.objects.count()
        unassigned_clients = Client.objects.filter(agent__isnull=True, is_converted=False).count()
        assigned_clients = Client.objects.filter(agent__isnull=False, is_converted=False).count()
        converted_clients = Client.objects.filter(agent__isnull=False, is_converted=True).count()

        context = {
            'total_client_count': total_client_count,
            'unassigned_clients': unassigned_clients,
            'assigned_clients': assigned_clients,
            'converted_clients': converted_clients
        }

        return render(request, 'dashboard.html', context)
