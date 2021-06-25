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
    def get(self, request):
        search_param = request.GET.get('q')
        client_type = request.GET.get('type')

        queryset = self._get_user_clients(user=request.user)
        queryset = self._filter_by_search_param(search_param, queryset)

        if client_type is None:
            client_type = 'assigned' if request.user.is_agent() else 'unassigned'

        queryset = self._filter_by_client_type(client_type, queryset)

        paginator = Paginator(queryset.order_by('id'), 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'clients': page_obj.object_list,
            'page_obj': page_obj,
            'client_type': client_type
        }

        return render(request, 'clients/list.html', context)

    def _filter_by_client_type(self, client_type, queryset):
        if client_type == 'unassigned':
            # Default unassigned clients list
            queryset = queryset.filter(agent__isnull=True, is_converted=False)
        elif client_type == 'assigned':
            queryset = queryset.filter(agent__isnull=False, is_converted=False)
        elif client_type == 'converted':
            queryset = queryset.filter(is_converted=True, agent__isnull=False)

        return queryset

    def _filter_by_search_param(self, search_param, queryset):
        if search_param:
            queryset = queryset.filter(
                Q(first_name__icontains=search_param) |
                Q(last_name__icontains=search_param) |
                Q(email__icontains=search_param)
            )
        return queryset

    def _get_user_clients(self, user):
        queryset = Client.objects.all()

        if user.is_agent():
            queryset = Client.objects.filter(agent=user.agent)
        elif user.is_business_owner():
            queryset = Client.objects.filter(business_owner=user.businessowner)

        return queryset


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
