from .base import BaseAgentTestCase


class AgentModelTests(BaseAgentTestCase):
    def test_str(self):
        self.assertEqual(self.agent1.user.username, 'agent1')
