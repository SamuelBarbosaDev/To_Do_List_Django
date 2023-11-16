from django.urls import path
from api.views import default, TaskList, TaskDetail

urlpatterns = [
    path('', default, name='default'),
    path('task/', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail')
]
