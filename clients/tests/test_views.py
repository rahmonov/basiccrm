from django.urls import reverse

from .base import BaseTestCase
from ..models import Client


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
