import datetime
from django.db import models
from django.utils import timezone
from users.models import Agent, BusinessOwner
from phonenumber_field.modelfields import PhoneNumberField


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
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=CHOICES, max_length=1)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_18_years_old(self):
        return (timezone.now() - datetime.timedelta(days=6588)) >= self.birthdate
