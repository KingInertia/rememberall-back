from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer, UserListSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created')
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserSerializer