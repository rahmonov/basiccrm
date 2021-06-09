from django.contrib import admin
from django.urls import path, include

from basiccrm.views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('users/', include('users.urls'), name='users'),
]
