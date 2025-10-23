from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Note, NoteImage, NoteHistory
from .serializers import NoteSerializer, NoteImageSerializer, NoteListSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import update_note_history

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
    
    def create(self, request):
            user = request.user
            title = request.data.get('title')
            
            if not title:
                return Response({"detail": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)

            note, created = Note.objects.get_or_create(
                user=user,
                title=title,
                defaults={
                    "content": request.data.get('content', ''),
                }
            )

            update_note_history(user, note)

            serializer = self.get_serializer(note)
            status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
            return Response(serializer.data, status=status_code)

    def retrieve(self, request):
        note = self.get_object()
        user = request.user
        update_note_history(user, note)
        serializer = self.get_serializer(note)
        return Response(serializer.data)

class NoteImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NoteImage.objects.all()
    serializer_class = NoteImageSerializer

    def get_queryset(self):
        user = self.request.user
        return NoteImage.objects.filter(note__user=user)
    
