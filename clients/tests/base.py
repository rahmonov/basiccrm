from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from clients.models import Client
from users.models import User, BusinessOwner


class BaseTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.user = User.objects.create(username='someuser')
        self.user.set_password('testpass')
        self.user.save()

        self.business_owner = BusinessOwner.objects.create(user=self.user)
        self.my_client = Client.objects.create(
            first_name='First',
            last_name='Last',
            birthdate=timezone.now(),
            email="someuser@gmail.com",
            address="Tashkent",
            phone_number="+998915228512",
            gender="M",
            profile_image=reverse(),
        )