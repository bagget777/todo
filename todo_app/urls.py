# todo_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, TodoViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
