from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'form'
    success_url = reverse_lazy('clients:index')
    template_name = 'clients/create.html'


class IndexView(ListView):
    queryset = Client.objects.all()
    template_name = 'clients/index.html'
    context_object_name = 'clients'


class ClientDeleteView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        context = {
            'client': client
        }
        return render(request=request, template_name='clients/delete_confirm.html', context=context)

    def post(self, request, id):
        client = get_object_or_404(Client, pk=id)

        client.delete()
        return redirect('clients:index')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/update.html'
    form_class = ClientForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('clients:index')


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    pk_url_kwarg = 'id'
    template_name = 'clients/detail.html'

