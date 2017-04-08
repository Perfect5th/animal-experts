from django.test import TestCase

# Create your tests here.
class URLTest(TestCase):
    urls = ['/', '/?q=test+search']
    
    def test_search_routes(self):
        for url in self.urls:
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
