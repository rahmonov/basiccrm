from .base import BaseTestCase


class ClientModelTestCase(BaseTestCase):
    def test_str_client_model(self):
        self.assertEqual(str(self.my_client), "First Last")
