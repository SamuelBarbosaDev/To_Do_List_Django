from rest_framework.permissions import AllowAny
from auth.serializers import AuthTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class AuthTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenObtainPairSerializer
