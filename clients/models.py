from django.db import models

from users.models import Agent, BusinessOwner


class Client(models.Model):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=CHOICES, max_length=1)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
