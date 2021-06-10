from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(ListView):
    queryset = Client.objects.all()
    template_name = 'clients/list.html'
    context_object_name = 'clients'


class ClientDetailedView(DetailView):
    queryset = Client.objects.all()
    template_name = 'clients/detailed_view.html'
    pk_url_kwarg = 'id'


class ClientCreateView(CreateView):
    form_class = ClientForm
    template_name = 'clients/create.html'

    def get_success_url(self):
        return reverse('clients:list')


class ClientDeleteView(View):
    def get(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            raise Http404()

        return render(request, 'clients/delete-confirm.html', {'client': client})

    def post(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            raise Http404()

        client.delete()
        messages.success(request, 'Client successfully deleted')

        return redirect(reverse('clients:list'))


class ClientUpdateView(UpdateView):
    queryset = Client.objects.all()
    template_name = 'clients/update.html'
    form_class = ClientForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('clients:list')
