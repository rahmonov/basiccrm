from django.contrib import admin

from users.models import User, BusinessOwner, Agent

admin.site.register(User)
admin.site.register(BusinessOwner)
admin.site.register(Agent)
