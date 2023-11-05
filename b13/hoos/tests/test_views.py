from django.test import TestCase, Client
from django.urls import reverse
from hoos.models import *
import json

class TestViews(TestCase):
    
    def test_home_GET(self):
        client = Client()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
