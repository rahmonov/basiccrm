from .base import BaseAgentTestCase
from django.shortcuts import reverse
from ..models import Agent


class AgentViewTests(BaseAgentTestCase):

    def test_agent_list_view_page(self):
        url = reverse('agents:list')
        self.client.login(username="someuser", password='testpass')
        res = self.client.get(url)

        self.assertContains(res, "Agents")
        self.assertEqual(res.status_code, 200)

    def test_agent_delete_view_GET_request(self):
        self.client.login(username='someuser', password='testpass')
        url = reverse('agents:delete', args=[self.agent1.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.agent1)

    def test_agent_delete_view_POST_request(self):
        self.client.login(username='someuser', password='testpass')
        url = reverse('agents:delete', args=[self.agent1.id])
        res = self.client.post(url, follow=True)

        self.assertRedirects(res, reverse('agents:list'), status_code=302, target_status_code=200)
        self.assertEqual(False, Agent.objects.filter(pk=self.agent1.id).exists())

    def test_agent_detail_view(self):
        self.client.login(username='someuser', password='testpass')
        url = reverse('agents:detail', args=[self.agent1.id])

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.agent1.user.first_name)
        self.assertContains(res, self.agent1.region)

