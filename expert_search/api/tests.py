import json

from rest_framework.test import APITestCase


class ExpertSearchTests(APITestCase):
    fixtures = ('one_user.json',)

    def test_search_term(self):
        """
        Ensure that we can get properly ranked results from the API when we use
        a specific search term.
        """
        search_term = 'exotic'
        response = self.client.get('/api/experts/?q=' + search_term)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content['count'], 2)
        results = content['results']
        self.assertIn(search_term , results[0]['subjects'].lower())
        self.assertNotIn(search_term, results[1]['subjects'].lower())
