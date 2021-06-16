from django.urls import path

from clients.views import ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView, ClientDetailView

app_name = 'clients'
urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('<int:id>/delete/', ClientDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', ClientDetailView.as_view(), name='detail'),
]
