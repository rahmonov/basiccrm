from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic.edit import DeleteView, UpdateView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(LoginRequiredMixin, View):
    def get_user_clients(self, user):
        queryset = Client.objects.all()

        if user.is_agent():
            queryset = Client.objects.filter(agent=user.agent)
        elif user.is_business_owner():
            queryset = Client.objects.filter(business_owner=user.businessowner)

        return queryset

    def get(self, request):
        search_param = request.GET.get('q')
        type_client = request.GET.get('type')

        queryset = self.get_user_clients(user=request.user)

        if search_param:
            queryset = queryset.filter(
                Q(first_name__icontains=search_param) |
                Q(last_name__icontains=search_param) |
                Q(email__icontains=search_param)
            )

        if type_client is None:
            type_client = 'unassigned'

        if type_client == 'unassigned':
            # Default unassigned clients list
            queryset = queryset.filter(agent__isnull=True, is_converted=False)
        elif type_client == 'assigned':
            queryset = queryset.filter(agent__isnull=False, is_converted=False)
        elif type_client == 'converted':
            queryset = queryset.filter(is_converted=True, agent__isnull=False)

        paginator = Paginator(queryset.order_by('id'), 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'clients': page_obj.object_list,
            'page_obj': page_obj,
            'type_client': type_client
        }

        return render(request, 'clients/list.html', context)


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


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/update.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')
    pk_url_kwarg = 'id'
