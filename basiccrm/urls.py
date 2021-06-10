from django.contrib import admin
from django.urls import path, include

from basiccrm.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('users/', include('users.urls'), name='users'),
]
