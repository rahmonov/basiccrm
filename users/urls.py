from django.urls import path
from .views import UserSignUpView

app_name = 'users'
urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='register'),
]