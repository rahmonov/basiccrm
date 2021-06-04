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

        return render(request, 'clients/create.html', context)


class ClientDeleteView(View):
    def get(self, request, id):
        client = Client.objects.get(id=id)
        client.delete()
        return redirect(reverse('clients:list'))