import datetime
from django.test import TestCase
from users.models import User, BusinessOwner, Agent
from clients.models import Client
from django.utils import timezone
from django.shortcuts import reverse


def create_user():
    return User(first_name="test_user", password="45154515FFF")


def create_business_owner(user):
    return BusinessOwner(user=user)


def create_agent(user, owner):
    return Agent(user=user, business_owner=owner)


def create_client(owner, agent, birthdate):
    return Client(
        business_owner=owner,
        agent=agent,
        first_name="fayyozbek",
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


class ClientModelTests(TestCase):
    def test_client_creation(self):
        user, owner, agent = create_users()
        birth_date = timezone.now()
        client = create_client(owner, agent, birth_date)
        client.save()
        self.assertEqual(client, Client.objects.first())

    def test_is_client_18_years_old_with_datenow(self):
        user, owner, agent = create_users()
        birth_date = timezone.now()
        client = create_client(owner, agent, birth_date)
        client.save()
        self.assertEqual(client.is_18_years_old(), False)

    def test_client_age_with_future_date(self):
        user, owner, agent = create_users()
        birth_date = timezone.now() + datetime.timedelta(days=3000)
        client = create_client(owner, agent, birth_date)
        client.save()
        self.assertEqual(client.is_18_years_old(), False)

    def test_client_age_with_18_years(self):
        user, owner, agent = create_users()
        birth_date = timezone.now() - datetime.timedelta(days=6588)
        client = create_client(owner, agent, birth_date)
        client.save()
        self.assertEqual(client.is_18_years_old(), True)


class ClientCreateViewTests(TestCase):
    def test_client_create_html_page_renders(self):
        url = reverse("clients:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create a client:")

    def test_client_create_html_post(self):
        url = reverse('clients:create', args=())


