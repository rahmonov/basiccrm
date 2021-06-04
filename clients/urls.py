from django.urls import path

from clients.views import ClientListView, ClientCreateView

app_name = 'clients'
urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create')
]
