from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def is_agent(self):
        return hasattr(self, 'agent')

    def is_business_owner(self):
        return hasattr(self, 'businessowner')


class BusinessOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agent: {self.user.username}"
