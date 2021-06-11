from django.urls import path
from .views import UserSignUpView, UserLoginView, UserLogoutView

app_name = 'users'
urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]