from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()

        context = {"clients": clients}

        return render(request, "clients/list.html", context)


class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()

        context = {"form": form}

        return render(request, "clients/create.html", context)

    def post(self, request):
        form = ClientForm(data=request.POST)

        context = {"form": form}

        if form.is_valid():
            form.save()
            return redirect(reverse("clients:index"))
        else:
            return render(request, "clients/create.html", context)


class IndexView(View):
    def get(self, request):
        clients_data = Client.objects.all()
        context = {"clients": clients_data}
        return render(request, "clients/index.html", context)


class ClientDeleteView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        client.delete()
        return redirect(reverse("clients:index"))


class ClientUpdateView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)

        form = ClientForm(instance=client)
        context = {
            'form': form
        }
        return render(request, 'clients/update.html', context)

    def post(self, request, id):
        client = get_object_or_404(Client, pk=id)
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('clients:index'))

        context = {
            'form': form
        }
        return render(request, 'clients/update.html', context)
