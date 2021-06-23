from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from agents.forms import AgentForm
from agents.models import Agent
from users.models import User


class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'agents/list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        if self.request.user.is_business_owner():
            return Agent.objects.filter(business_owner=self.request.user.businessowner)


class AgentCreateView(LoginRequiredMixin, View):

    def get(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(initial={'business_owner':business_owner})
        context = {
            'form': form
        }

        return render(request, 'agents/create.html', context)

    def post(self, request):
        form = AgentForm(data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            region = form.cleaned_data['region']
            business_owner = form.cleaned_data['business_owner']

            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
                )

            agent = Agent.objects.create(
                user=user,
                business_owner=business_owner,
                region=region
            )

            return redirect(reverse('agents:list'))
        else:
            return render(request, 'agents/create.html', context)