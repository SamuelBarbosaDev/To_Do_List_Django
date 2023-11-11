import json
from django.test import TestCase
from rest_framework import status


class ApiTestCase(TestCase):
    def setUp(self):
        pass

    def test_request_to_default_api(self):
        response = self.client.get(r'/api/')

        data = json.loads(response.content)
        self.assertEqual(data, {'Funcionou': 1})

    def test_default_api_request_status(self):
        response = self.client.get(r'/api/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
