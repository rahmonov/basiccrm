from django.contrib import admin

from clients.models import Client


class ClientModelAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(Client, ClientModelAdmin)
