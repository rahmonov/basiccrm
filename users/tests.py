import datetime

from django.test import TestCase
from .models import User, BusinessOwner, Agent
from clients.models import Client
from django.utils import timezone


def create_user():
    return User(first_name="test_user", password='45154515FFF')


def create_business_owner(user):
    return BusinessOwner(user=user)


def create_agent(user, owner):
    return Agent(user=user, business_owner=owner)


def create_client(owner, agent, birthdate):
    return Client(
        business_owner=owner,
        agent=agent,
        first_name='fayyozbek',
        last_name="berdiyorov",
        birthdate=birthdate,
        email="dsfkljd@gmail.com",
        phone_number="5164165165",
        address="sigfjvnlm",
        gender="M",
    )


def create_users():
    user = create_user()
    user.save()
    owner = create_business_owner(user)
    owner.save()
    agent = create_agent(user, owner)
    agent.save()

    return user, owner, agent


class UserModelTests(TestCase):
    def test_user_creation(self):
        user = create_user()
        user.save()
        self.assertEqual(user, User.objects.first())

    def test_business_owner_creation(self):
        user = create_user()
        user.save()
        owner = create_business_owner(user)
        owner.save()

        self.assertEqual(owner, BusinessOwner.objects.first())

    def test_agent_creation(self):
        user, owner, agent = create_users()
        self.assertEqual(agent, Agent.objects.first())


