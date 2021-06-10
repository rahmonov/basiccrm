from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from clients.models import Client
from users.models import User, BusinessOwner


class ClientBaseTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username='user')
        self.business_owner = BusinessOwner.objects.create(user=self.user)
        self.my_client = Client.objects.create(
            business_owner=self.business_owner,
            first_name='First',
            last_name='Last',
            email='some@gmail.com',
            birthdate=timezone.now() - timedelta(days=2000),
            phone_number='+4917786374343',
            address='Some Addr',
            gender='M'
        )