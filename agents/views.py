from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
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
        form = AgentForm(initial={'business_owner': business_owner})
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


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    model = Agent
    context_object_name = "agent"
    success_url = reverse_lazy('agents:list')
    template_name = 'agents/delete_confirm.html'
    pk_url_kwarg = "id"
