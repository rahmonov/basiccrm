from django.core.exceptions import ObjectDoesNotExist
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

    def test_delete_view_GET_method(self):
        """Test that client view is working and page is rendered"""
        self.client.login(username=self.user.username, password='testpass')
        link = reverse('clients:delete', args=[self.my_client.id])
        res = self.client.get(link)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, str(self.my_client))

    def test_delete_view_POST_method(self):
        """Test that client is deleted """
        self.client.login(username=self.user.username, password='testpass')
        link = reverse('clients:delete', args=[self.my_client.id])
        res = self.client.post(link)
        self.assertEqual(res.status_code, 302)
        with self.assertRaises(ObjectDoesNotExist):
            Client.objects.get(pk=self.my_client.id)
