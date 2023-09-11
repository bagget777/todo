from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import CustomUser, Todo
from .serializers import CustomUserSerializer, TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import action


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):

        user = self.request.user

        queryset = Todo.objects.filter(user=user)

        return queryset

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):

        user = self.request.user

        Todo.objects.filter(user=user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


