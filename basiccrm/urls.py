from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('users/', include('users.urls'))
]
