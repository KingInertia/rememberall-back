from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, NoteImage, NoteListSerializer
from .serializers import NoteSerializer, NoteImageSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return NoteListSerializer
        return NoteSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NoteImage.objects.all()
    serializer_class = NoteImageSerializer

    def get_queryset(self):
        user = self.request.user
        return NoteImage.objects.filter(note__user=user)
    
