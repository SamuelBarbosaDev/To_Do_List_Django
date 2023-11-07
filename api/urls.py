from django.urls import path
from api.views import default

urlpatterns = [
    path('', default, name='default'),
]
