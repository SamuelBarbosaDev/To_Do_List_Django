from ..models import Task
from django.test import TestCase


class TaskTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='task 1',
            done=False,
            describe='Working to complete the task.'
        )

    def test_get_taks(self):
        task = Task.objects.get(title='task 1')
        self.assertEqual(task, self.task)
