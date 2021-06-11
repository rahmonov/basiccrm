from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from clients.forms import ClientForm
from clients.models import Client


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
        context = {
            'client': client
        }
        return render(request=request, template_name='clients/delete_confirm.html', context=context)

    def post(self, request, id):
        client = get_object_or_404(Client, pk=id)

        client.delete()
        return redirect('clients:index')


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
        form = ClientForm(
            data=request.POST,
            instance=client
        )
        if form.is_valid():
            form.save()

            return redirect(reverse('clients:index'))

        context = {
            'form': form
        }
        return render(request, 'clients/update.html', context)


class ClientDetailView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        context = {
            'client': client
        }
        return render(request, 'clients/detail.html', context)