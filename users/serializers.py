from rest_framework import serializers
from notes.models import NoteHistory

from .models import User

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializer(serializers.ModelSerializer):
    notes_history = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'notes_history']

    def get_notes_history(self, obj):
        history = NoteHistory.objects.filter(user=obj).select_related('note')
        return [
            {
                'id': h.note.id,
                'title': h.note.title
            }
            for h in history
        ]
