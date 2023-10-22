from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hoos.views import home, logout_view, map


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_map_url_resolves(self):
        url = reverse('map')
        self.assertEquals(resolve(url).func, map)
