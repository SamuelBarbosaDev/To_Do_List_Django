from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=60)
    done = models.BooleanField(default=False)
    describe = models.TextField(max_length=600, blank=True)
