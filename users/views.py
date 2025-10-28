from rest_framework import viewsets 
from .models import User
from .serializers import UserPublicSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.only('id', 'username')
    serializer_class = UserPublicSerializer
