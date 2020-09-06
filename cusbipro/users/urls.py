"""
=======================================
Routers for users app:
=======================================
"""

# Django
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

# Local app crud
from users import views

urlpatterns = [
    path('register/', views.CreateUser.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
