from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def test_home_GET(self):
        client = Client()

        # response = client.get(reverse('home'))

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'home.html')

class TestAdminViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.client.login(username='petertessier', password='Co$moBrown')

    # def test_test(self):
    #     response = self.client.get(reverse('home_admin'))

    #     self.assertEquals(response.status_code, 200)
