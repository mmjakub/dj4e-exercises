from django.test import TestCase
from django.urls import reverse

def assertContainsRevUrl(self, viewname):
    res = self.client.get('/')
    url = reverse(viewname)
    self.assertContains(res, f'href="{url}"')

class HomeViewTests(TestCase):
    def test_links_to_polls(self):
        '''
        The link to Polls app is displayed
        '''
        assertContainsRevUrl(self, 'polls:index')

    def test_links_to_hello(self):
        '''
        The link to hello app is displayed
        '''
        assertContainsRevUrl(self, 'hello:index')
