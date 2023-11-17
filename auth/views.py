from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from auth.serializers import (
    AuthTokenObtainPairSerializer,
    RegisterSerializer
)


class AuthTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
