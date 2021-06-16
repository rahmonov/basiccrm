from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from clients.forms import ClientForm
from clients.models import Client

"""
Homework

1. Add ClientDetailView
2. Tests for all views
"""


class ClientListView(ListView):
    queryset = Client.objects.all()
    template_name = 'clients/list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    # queryset = get_object_or_404(Client, pk=id)
    model = Client
    template_name = 'clients/detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    form_class = ClientForm
    queryset = Client.objects.all()
    template_name = 'clients/create.html'


    def form_valid(self, form):
        return super().form_valid(form)

'''
class ClientUpdateView(UpdateView):
    form_class = ClientForm
    queryset = Client.objects.all()
    template_name = 'clients/create.html'

    def get_object(self):
        id_ =  self.kwargs.get("id")
        return get_object_or_404(Client, id=id_)

'''

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/update.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')

'''
class ClientUpdateView(View):
    def get(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            raise Http404()

        form = ClientForm(instance=client)

        context = {
            'form': form
        }

        return render(request, 'clients/update.html', context)

    def post(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            raise Http404()

        form = ClientForm(
            instance=client,
            data=request.POST
        )

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect(reverse('clients:list'))

        return render(request, 'clients/create.html', context)
'''



'''
class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()

        context = {
            'clients': clients
        }

        return render(request, 'clients/list.html', context)
'''


'''
class ClientDetailView(View):
    def get(self, request, id):
        client = Client.objects.get(pk=id)

        context = {
            'client': client
        }

        return render(request, 'clients/detail.html', context)
'''


'''
class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()

        context = {
            'form': form
        }

        return render(request, 'clients/create.html', context)

    def post(self, request):
        form = ClientForm(data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect(reverse('clients:list'))
        else:
            return render(request, 'clients/create.html', context)

'''



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

