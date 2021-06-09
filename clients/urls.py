from django.urls import path

from clients.views import ClientListView, ClientCreateView, IndexView, ClientDeleteView, ClientUpdateView

app_name = 'clients'
urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('index/', IndexView.as_view(), name='index'),
    path('<int:id>/delete/', ClientDeleteView.as_view(), name='delete'),
    path('<int:id>/update/', ClientUpdateView.as_view(), name='update'),
]
