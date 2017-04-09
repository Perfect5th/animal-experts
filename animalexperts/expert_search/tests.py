from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
class URLTest(TestCase):
    urls = ['/', '/?q=test+search']
    
    def test_search_routes(self):
        for url in self.urls:
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)


class ContributorTest(TestCase):
    fixtures = ['one_user.json']
    
    def test_contributor_login_logout(self):
        r = self.client.get('/contribute/login/')
        self.assertEqual(r.status_code, 200)
        
        r = self.client.post('/contribute/login/', data={'username': 'mitch',
            'password': 'superexample'})
        self.assertEqual(r.status_code, 302)
        
        r = self.client.get('/contribute/logout/')
        self.assertEqual(r.status_code, 302)
    
    def test_contributor_change_password(self):
        user = User.objects.get(pk=1)
        old_pass = user.password
        
        self.assertTrue(self.client.login(username='mitch',
            password='superexample'))
        
        r = self.client.get('/contribute/password_change/')
        self.assertEqual(r.status_code, 200)
        
        data = {'old_password': 'superexample', 'new_password1':
            'superexample2', 'new_password2': 'superexample2'}
        r = self.client.post('/contribute/password_change/', data=data)
        self.assertEqual(r.status_code, 302)
        user.refresh_from_db()
        new_pass = user.password
        self.assertNotEqual(old_pass, new_pass)
        
        r = self.client.get('/contribute/password_change_done/')
        self.assertEqual(r.status_code, 200)
