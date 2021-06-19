from django.urls import path

from agents.views import AgentListView, AgentCreateView

app_name = 'agents'
urlpatterns = [
    path('', AgentListView.as_view(), name='list'),
    path('create/', AgentCreateView.as_view(), name='create'),
]