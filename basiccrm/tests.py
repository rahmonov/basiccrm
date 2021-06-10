from django.test import TestCase
from django.urls import reverse


class LandingViewTestCase(TestCase):
    def test_landing(self):
        response = self.client.get(reverse('landing'))

        self.assertEqual(response.status_code, 200)
