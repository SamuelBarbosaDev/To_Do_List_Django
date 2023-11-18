from decouple import config
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


TEST_USER = config('TEST_USER', default='user')
TEST_PASSWORD = config('TEST_PASSWORD', default='******')
TEST_EMAIL = config('TEST_EMAIL', default='user@user.com')


class AuthStatusCodeTestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication:
        self.user = User.objects.create_user(
            username=TEST_USER,
            password=TEST_PASSWORD
        )

    def test_singup(self):
        serializer_singup = {
            'username': f'singup_{TEST_USER}',
            'password': f'{TEST_PASSWORD}',
            'password2': f'{TEST_PASSWORD}',
            'email': f'singup_{TEST_EMAIL}',
            'first_name': 'user',
            'last_name': 'test',
        }
        response = self.client.post(
            path=reverse('singup'),
            data=serializer_singup,
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg='Failed to create user.'
        )

    def test_login(self):
        serializer_login = {
            'username': f'{TEST_USER}',
            'password': f'{TEST_PASSWORD}',
        }

        response = self.client.post(
            path=reverse('login'),
            data=serializer_login,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg='Failed to sign in with user.'
        )

    def test_login_refresh(self):
        serializer_login = {
            'username': f'{TEST_USER}',
            'password': f'{TEST_PASSWORD}',
        }

        response_login = self.client.post(
            path=reverse('login'),
            data=serializer_login,
            format='json',
        )

        self.assertEqual(
            response_login.status_code,
            status.HTTP_200_OK,
            msg='Failed to sign in with user.'
        )

        # Extract the update token
        refresh_token = response_login.data.get('refresh', None)

        self.assertIsNotNone(refresh_token, msg='Refresh token not found in login response.')

        # Use the update token to obtain a new access token
        response_refresh = self.client.post(
            path=reverse('login_refresh'),
            data={'refresh': refresh_token},
            format='json',
        )

        self.assertEqual(
            response_refresh.status_code,
            status.HTTP_200_OK,
            msg=f'Failed to refresh token. Response: {response_refresh.data}'
        )
