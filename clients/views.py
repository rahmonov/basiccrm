from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'form'
    success_url = reverse_lazy('clients:index')
    template_name = 'clients/create.html'


class IndexView(LoginRequiredMixin, ListView):
    queryset = Client.objects.all()
    template_name = 'clients/index.html'
    context_object_name = 'clients'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/delete_confirm.html'
    success_url = reverse_lazy('clients:index')
    pk_url_kwarg = 'id'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'clients/update.html'
    form_class = ClientForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('clients:index')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'
    pk_url_kwarg = 'id'
    template_name = 'clients/detail.html'

