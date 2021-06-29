from django.urls import path

from api.views import ClientListAPIView, ClientDetailAPIView


app_name = 'api'
urlpatterns = [
    path('clients/', ClientListAPIView.as_view(), name='clients-list'),
    path('clients/<int:id>/', ClientDetailAPIView.as_view(), name='client-detail'),
]
