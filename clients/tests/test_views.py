from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone

from users.models import User, BusinessOwner
from .base import BaseTestCase
from ..models import Client


class ClientViewTestCase(BaseTestCase):
    def test_fail(self):
        assert 1 == 3

    def test_list_for_business_owner(self):
        self.client.login(username='someuser', password='testpass')
        user2 = User.objects.create(username='someuser2')
        business_owner2 = BusinessOwner.objects.create(user=user2)
        Client.objects.create(
            business_owner=business_owner2,
            first_name='Second',
            last_name='LastName',
            birthdate=timezone.now(),
            email='jrahm2@gmail.com',
            address='SomeAddr2',
            phone_number='+49123123212123',
            gender='M'
        )

        response = self.client.get(reverse('clients:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Last')
        self.assertContains(response, '+4912312321')
        self.assertNotContains(response, 'Second LastName')
        self.assertNotContains(response, '+49123123212123')

    def test_create(self):
        self.client.login(username='someuser', password='testpass')

        payload = {
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
