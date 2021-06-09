from django.urls import path

from users.views import RegisterView


app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
