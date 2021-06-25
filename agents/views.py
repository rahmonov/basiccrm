from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView

from agents.forms import AgentForm
from agents.models import Agent
from users.models import User


class AgentListView(LoginRequiredMixin, View):
    def get(self, request):
        search_param = request.GET.get('q')
        agent_type = request.GET.get('type')
        queryset = Agent.objects.all()

        if request.user.is_business_owner():
            queryset = Agent.objects.filter(business_owner=request.user.businessowner)

        if search_param:
            queryset = queryset.filter(Q(user__username__icontains=search_param))

        paginator = Paginator(queryset.order_by('id'), 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'agents': page_obj.object_list,
            'page_obj': page_obj,
        }

        return render(request, 'agents/list.html', context)

      
class AgentCreateView(LoginRequiredMixin, View):

    def get(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(initial={'business_owner':business_owner})
        
        context = {
            'form': form
        }

        return render(request, 'agents/create.html', context)

    def post(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            region = form.cleaned_data['region']

            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            Agent.objects.create(
                user=user,
                business_owner=business_owner,
                region=region
            )

            return redirect(reverse('agents:list'))
        else:
            return render(request, 'agents/create.html', context)
          

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    model = Agent
    context_object_name = "agent"
    success_url = reverse_lazy('agents:list')
    template_name = 'agents/delete_confirm.html'
    pk_url_kwarg = "id"

