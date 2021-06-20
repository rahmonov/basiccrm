from django.contrib import admin

from users.models import User, BusinessOwner
from agents.models import Agent

admin.site.register(User)
admin.site.register(BusinessOwner)
admin.site.register(Agent)
