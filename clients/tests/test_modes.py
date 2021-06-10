from .base import ClientBaseTestCase


class ClientModelTestCase(ClientBaseTestCase):
    def test_str(self):
        self.assertEqual(str(self.my_client), 'First Last')
