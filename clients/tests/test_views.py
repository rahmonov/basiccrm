from django.urls import reverse

from .base import ClientBaseTestCase


class ClientViewTestCase(ClientBaseTestCase):
    def test_list_view(self):
        response = self.client.get(reverse('clients:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.my_client)
