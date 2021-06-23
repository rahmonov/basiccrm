from django.test import TestCase

from agents.models import Agent
from users.models import User, BusinessOwner


class BaseAgentTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.user = User.objects.create(username='someuser')
        self.user.set_password("testpass")
        self.user.save()

        self.business_owner = BusinessOwner.objects.create(user=self.user)

        self.user_for_agent = User.objects.create(username='agent1')
        self.user.set_password('testpass')
        self.user_for_agent.save()
        self.agent1 = Agent.objects.create(user=self.user_for_agent, business_owner=self.business_owner)
