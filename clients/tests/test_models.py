from .base import BaseTestCase


class ClientModelTestCase(BaseTestCase):
    def test_str(self):
        self.assertEqual(str(self.my_client), 'First Last')
