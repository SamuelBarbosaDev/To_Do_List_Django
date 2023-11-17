from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token, AuthUser


class AuthTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super(AuthTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
