from rest_framework import serializers
from notes.models import NoteHistory

from .models import User

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializer(serializers.ModelSerializer):
    recent_notes = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'recent_notes']

    def get_recent_notes(self, obj):
        history = NoteHistory.objects.filter(user=obj).select_related('note')
        return [
            {
                'id': h.note.id,
                'title': h.note.title
            }
            for h in history
        ]
