from django.test import TestCase
from django.urls import reverse
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


class ClientModelTestCase(BaseTestCase):
    def test_str(self):
        self.assertEqual(str(self.my_client), 'First Last')


class ClientViewTestCase(BaseTestCase):
    def test_list(self):
        response = self.client.get(reverse('clients:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Last')
        self.assertContains(response, '+4912312321')

    def test_create(self):
        payload = {
            'business_owner': self.business_owner.pk,
            'first_name': 'First',
            'last_name': 'Last',
            'address': 'addr',
            'phone_number': '+4313213',
            'email': 'asdsa@gmail.com',
            'birthdate': '04/04/1994',
            'gender': 'M'
        }

        response = self.client.post(
            reverse('clients:create'), data=payload, follow=True
        )

        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(response.status_code, 200)
