from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from auth.views import (
    AuthTokenObtainPairView,
    RegisterView
)


urlpatterns = [
    path('login/', AuthTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('singup/', RegisterView.as_view(), name='singup')
]
