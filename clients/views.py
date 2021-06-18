from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'clients/index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        if self.request.user.is_agent():
            print("Sending agent clients")
            return Client.objects.filter(agent=self.request.user.agent)
        elif self.request.user.is_business_owner():
            print("Sending business owner clients")
            return Client.objects.filter(business_owner=self.request.user.businessowner)
        else:
            print("Sending all clients")
            return Client.objects.all()


class ClientDetailedView(LoginRequiredMixin, View):
    def get(self, request, id):
        client = Client.objects.get(pk=id)

        context = {
            'client': client
        }

        return render(request, 'clients/detailed_view.html', context)


class ClientCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ClientForm()

        context = {
            'form': form
        }

        return render(request, 'clients/create.html', context)

    def post(self, request):
        form = ClientForm(data=request.POST, files=request.FILES)

        context = {
            'form': form
        }

        if form.is_valid():
            business_owner = request.user.businessowner

            client = form.save(commit=False)
            client.business_owner = business_owner
            client.save()

            return redirect(reverse('clients:list'))
        else:
            return render(request, 'clients/create.html', context)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/delete-confirm.html'
    success_url = reverse_lazy('clients:list')
    pk_url_kwarg = 'id'


class ClientUpdateView(LoginRequiredMixin, View):
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
            data=request.POST,
            files=request.FILES
        )

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect(reverse('clients:list'))

        return render(request, 'clients/create.html', context)

