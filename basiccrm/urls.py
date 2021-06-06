from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('crm/home/', include('pages.urls')),
]
