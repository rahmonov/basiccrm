from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from users.models import Agent


class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'agents/list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        if self.request.user.is_business_owner():
            return Agent.objects.filter(business_owner=self.request.user.businessowner)


    # def get_queryset(self):
    #     if self.request.user.is_agent():
    #         print("Sending agent clients")
    #         return Client.objects.filter(agent=self.request.user.agent)
    #     elif self.request.user.is_business_owner():
    #         print("Sending business owner clients")
    #         return Client.objects.filter(business_owner=self.request.user.businessowner)
    #     else:
    #         print("Sending all clients")
    #         return Client.objects.all()
