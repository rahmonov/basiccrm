from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect(reverse('clients:index'))

        return render(request, 'clients/create.html', context)


class IndexView(View):
    def get(self, request):
        clients_data = Client.objects.all()
        context = {
            'clients': clients_data
        }
        return render(request, 'clients/index.html', context)


class ClientDeleteView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        client.delete()
        return redirect(reverse('clients:index'))


def update(request, id):
    client = get_object_or_404(Client, pk=id)

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client.first_name = form.cleaned_data['first_name']
            client.last_name = form.cleaned_data['last_name']
            client.business_owner = form.cleaned_data['business_owner']
            client.agent = form.cleaned_data['agent']
            client.profile_picture = form.cleaned_data['profile_picture']
            client.address = form.cleaned_data['address']
            client.gender = form.cleaned_data['gender']
            client.phone_number = form.cleaned_data['phone_number']
            client.email = form.cleaned_data['email']
            client.birthdate = form.cleaned_data['birthdate']
            client.save()

            return redirect(reverse('clients:index'))
    else:
        form = ClientForm(instance=client)

    context = {
        'form': form
    }
    return render(request, 'clients/create.html', context)


# TODO: clarify why class based view does not work with updating client
# class ClientUpdateView(View):
#     def get(self, request, id):
#         client = get_object_or_404(Client, pk=id)
#
#         if request.method == 'POST':
#             form = ClientForm(request.POST)
#             if form.is_valid():
#
#                 client.first_name = form.cleaned_data['first_name']
#                 client.last_name = form.cleaned_data['last_name']
#                 client.business_owner = form.cleaned_data['business_owner']
#                 client.agent = form.cleaned_data['agent']
#                 client.profile_picture = form.cleaned_data['profile_picture']
#                 client.address = form.cleaned_data['address']
#                 client.gender = form.cleaned_data['gender']
#                 client.phone_number = form.cleaned_data['phone_number']
#                 client.email = form.cleaned_data['email']
#                 client.birthdate = form.cleaned_data['birthdate']
#                 client.save()
#
#                 return redirect(reverse('clients:index'))
#         else:
#             form = ClientForm(instance=client)
#         context = {
#             'form': form
#         }
#         return render(request, 'clients/update.html', context)
