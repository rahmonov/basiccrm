from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from agents.forms import AgentForm
from agents.models import Agent
from users.models import User


class AgentListView(LoginRequiredMixin, View):
    def get(self, request):
        # search_param = request.GET.get('q')
        agent_type = request.GET.get('type')
        queryset = Agent.objects.all()

        if request.user.is_business_owner():
            queryset = Agent.objects.filter(business_owner=request.user.businessowner)

        if agent_type == "unassigned":
            queryset = queryset.filter(client__isnull=True)
        elif agent_type == "assigned":
            queryset = queryset.filter(client__isnull=False).distinct()

        paginator = Paginator(queryset.order_by('id'), 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'agents': page_obj.object_list,
            'page_obj': page_obj,
        }

        return render(request, 'agents/index.html', context)


class AgentCreateView(LoginRequiredMixin, View):

    def get(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(initial={'business_owner':business_owner})
        form.fields['user'].queryset = User.objects.filter(agent__isnull=True)
        context = {
            'form': form
        }

        return render(request, 'agents/create.html', context)

    def post(self, request):
        form = AgentForm(data=request.POST, files=request.FILES)

        context = {
            'form': form
        }

        if form.is_valid():
            business_owner = request.user.businessowner
            agent = form.save(commit=False)
            agent.business_owner = business_owner
            agent.save()

            return redirect(reverse('agents:list'))
        else:
            return render(request, 'agents/create.html', context)

