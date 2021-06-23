from .base import BaseAgentTestCase
from django.shortcuts import reverse


class AgentViewTests(BaseAgentTestCase):

    def test_agent_list_view_page(self):
        url = reverse('agents:list')
        self.client.login(username="someuser", password='testpass')
        res = self.client.get(url)

        self.assertContains(res, 'agent1')
        self.assertContains(res, "Agents")
        self.assertEqual(res.status_code, 200)
