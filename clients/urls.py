from django.urls import path

from clients.views import ClientListView, ClientCreateView, IndexView, ClientDeleteView, ClientUpdateView

app_name = 'clients'
urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('index/', IndexView.as_view(), name='index'),
    path('delete/<int:id>/', ClientDeleteView.as_view(), name='delete'),
    path('update/<int:id>/', ClientUpdateView.as_view(), name='update'),
]
