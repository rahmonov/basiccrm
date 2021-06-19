from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from basiccrm.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('crm/clients/', include('clients.urls'), name='clients'),
    path('crm/agents/', include('agents.urls'), name='agents'),
    path('users/', include('users.urls'), name='users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
