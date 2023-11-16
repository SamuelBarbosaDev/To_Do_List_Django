from .models import Task
from django.http import JsonResponse
from .serializer import TaskSerializer
from rest_framework import (
    generics,
    permissions,
)


def default(request):
    return JsonResponse({'Funcionou': 1})


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
