from django.test import TestCase
from django.utils import timezone

from clients.models import Client
from users.models import User, BusinessOwner


class BaseTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.user = User.objects.create(username='someuser')
        self.business_owner = BusinessOwner.objects.create(user=self.user)
        self.my_client = Client.objects.create(
            business_owner=self.business_owner,
            first_name='First',
            last_name='Last',
            birthdate=timezone.now(),
            email='jrahm@gmail.com',
            address='SomeAddr',
            phone_number='+4912312321',
            gender='M'
        )
