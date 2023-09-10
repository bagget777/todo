# todo_app/serializers.py

from rest_framework import serializers
from .models import CustomUser, Todo

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'created_at']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'age', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
