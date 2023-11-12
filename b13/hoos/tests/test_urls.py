from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from hoos.views import home, logout_view


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_logout_status(self):
        c = Client()
        response = c.get('/logout/')
        self.assertEquals(response.status_code, 302)
        # self.assertGreaterEqual(400, response.status_code)
