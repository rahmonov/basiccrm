from django.db import models

from users.models import User, BusinessOwner


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
    region = models.CharField(max_length=100, default='Uzbekistan')

    def __str__(self):
        return f"Agent: {self.user.username}"
