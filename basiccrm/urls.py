from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    path('', include('pages.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('users/', include('users.urls'), name='users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
