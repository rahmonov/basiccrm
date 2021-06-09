from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()

        context = {
            'clients': clients
        }

        return render(request, 'clients/list.html', context)


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
