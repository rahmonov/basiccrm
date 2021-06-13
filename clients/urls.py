from django.urls import path

from clients.views import ClientCreateView, IndexView, ClientDeleteView, ClientDetailView, ClientUpdateView

app_name = 'clients'
urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create'),
    path('index/', IndexView.as_view(), name='index'),
    path('<int:id>/delete/', ClientDeleteView.as_view(), name='delete'),
    path('<int:id>/update/', ClientUpdateView.as_view(), name='update'),
    path('<int:id>/detail/', ClientDetailView.as_view(), name='detail'),

]
