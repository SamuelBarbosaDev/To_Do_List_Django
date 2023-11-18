from ..models import Task
from decouple import config
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


TEST_USER = config('TEST_USER', default='user')
TEST_PASSWORD = config('TEST_PASSWORD', default='******')


class BusinessRuleTestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication:
        self.user = User.objects.create_user(
            username=TEST_USER,
            password=TEST_PASSWORD
        )

        # Authenticate the user
        response = self.client.post(
            path=reverse('login'),
            data={'username': TEST_USER, 'password': TEST_PASSWORD},
            format='json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg='Failed to sign in with user.'
        )

        # JWT token:
        self.token = response.data['access']

        # Creating tasks:
        self.task = Task.objects.create(
            id=1,
            title='Training',
            done=False,
            describe='Afternoon training',
        )

    def test_add_tasks(self):
        serializer_task = {
            'title': 'task 1',
            'done': False,
            'describe': 'Working to complete the task.',
        }

        response = self.client.post(
            path=f'/api/task/?username={TEST_USER}',
            data=serializer_task,
            format='json',
            headers={'Authorization': f'Bearer {self.token}'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg='Failed to create a task.'
        )

    def test_list_tasks(self):
        response = self.client.get(
            path=f'/api/task/?username={TEST_USER}',
            headers={'Authorization': f'Bearer {self.token}'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mark_task_as_done(self):
        serializer_task = {
            'done': True,
        }

        response = self.client.patch(
            path=f'/api/task/1/?username={TEST_USER}',
            data=serializer_task,
            format='json',
            headers={'Authorization': f'Bearer {self.token}'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg='Failed to change task to done.'
        )

    def test_update_task(self):
        serializer_task = {
            'title': 'new task',
            'done': True,
            'describe': 'Done ;)',
        }

        response = self.client.put(
            path=f'/api/task/1/?username={TEST_USER}',
            data=serializer_task,
            format='json',
            headers={'Authorization': f'Bearer {self.token}'},
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg='Failed to update the task.'
        )

    def test_delete_task(self):
        response = self.client.delete(
            path=f'/api/task/1/?username={TEST_USER}/',
            headers={'Authorization': f'Bearer {self.token}'},
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            msg='Failed to delete task.'
        )
