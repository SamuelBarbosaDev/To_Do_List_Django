from decouple import config
from ..models import Task
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


TEST_USER = config('TEST_USER', default='user')
TEST_PASSWORD = config('TEST_PASSWORD', default='******')


class TestBusinessRule(APITestCase):
    def setUp(self):
        # Create a user for authentication:
        self.user = User.objects.create_user(
            username=TEST_USER,
            password=TEST_PASSWORD
        )

        # Authenticate the user
        self.client.login(
            username=TEST_USER,
            password=TEST_PASSWORD
        )

        # Creating tasks:
        self.task = Task.objects.create(
            id=1,
            title='Training',
            done=False,
            describe='Afternoon training',
        )

    def test_sign_up_a_user(self):
        serializer_user = {
            'username': 'user',
            'email': 'user@email.com',
            'password': '****',
        }

        self.client.post(
            path=r'/api/singup/',
            data=serializer_user,
            format='json',
        )

        user = User.objects.get(email='user@email.com')

        self.assertEqual(
            serializer_user['username'],
            user.username,
            msg="Failed to create user."
        )

    def test_login_a_user(self):
        serializer_login = {
            'username': f'{TEST_USER}',
            'password': f'{TEST_PASSWORD}',
        }

        response = self.client.post(
            path=r'/api/login/',
            data=serializer_login,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg='Failed to sign in with user.'
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
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg='Failed to create a task.'
        )

    def test_list_tasks(self):
        response = self.client.get(
            path=f'/api/task/?username={TEST_USER}'
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
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg='Failed to update the task.'
        )

    def test_delete_task(self):
        response = self.client.delete(
            path=f'/api/task/1/?username={TEST_USER}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            msg='Failed to delete task.'
        )
