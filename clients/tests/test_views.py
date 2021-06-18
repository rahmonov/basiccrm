from .base import BaseTestCase
from django.urls import reverse_lazy, reverse
from clients.models import Client


class ClientViewTestCase(BaseTestCase):
    def test_list_of_clients(self):
        """Test that the list of clients in dashboard is rendering"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse_lazy("clients:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.my_client.first_name)
        self.assertContains(response, self.my_client.email)

    def test_client_create_view_template_is_rendering(self):
        """Test that the template for create view is being rendered"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse('clients:create')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_client_create_post_request(self):
        """Test that creating client with post request is working"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse_lazy('clients:create')
        payload = {
            'business_owner': self.business_owner.pk,
            'first_name': "First",
            'last_name': "Last",
            'birthdate': "05/05/2001",
            'email': "user@gmail.com",
            'phone_number_0': "+998",
            'phone_number_1': "915228512",
            'address': "Tashkent",
            'gender': "M",
        }

        response = self.client.post(url, data=payload)
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(response.status_code, 302)
        expected_url = reverse_lazy('clients:index')
        self.assertRedirects(response, expected_url=expected_url, status_code=302, target_status_code=200)

    def test_delete_template_is_rendering(self):
        """Test that the delete get request is working and template is being rendered"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse('clients:delete', args=[self.my_client.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, str(self.my_client))

    def test_client_delete_view(self):
        """Test that client delete view deletes the client"""
        self.client.login(username=self.user.username, password='testpass')

        url_delete = reverse('clients:delete', args=[self.my_client.id])
        response = self.client.post(url_delete)

        self.assertEqual(list(Client.objects.all()), [])

    def test_client_update_view_template_is_rendering(self):
        """Test that the template for client updating is being rendered
         and the actual data is present in the form"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse('clients:update', args=[self.my_client.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.my_client.first_name)
        self.assertContains(res, self.my_client.email)

    def test_update_view_is_updating_client(self):
        """Test that checks if the updated client is being saved into the database"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse('clients:update', args=[self.my_client.id])
        payload = {
            'business_owner': self.business_owner.pk,
            'first_name': "Fayyoz",
            'last_name': "Last",
            'birthdate': "05/05/2001",
            'email': "fayyoz@gmail.com",
            'phone_number_0': "+998",
            'phone_number_1': "915228512",
            'address': "Tashkent",
            'gender': "M",
        }
        res = self.client.post(url, data=payload, follow=True)
        self.assertRedirects(res, reverse('clients:index'), status_code=302, target_status_code=200)
        self.assertEqual(Client.objects.first().first_name, payload['first_name'])

    def test_client_detail_view(self):
        """Test that the client detail view is being rendered"""
        self.client.login(username=self.user.username, password='testpass')

        url = reverse('clients:detail', args=[self.my_client.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.my_client.first_name)






