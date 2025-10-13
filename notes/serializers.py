from rest_framework import serializers
from .models import Note, NoteImage


class NoteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteImage
        fields = ('id', 'image')


class NoteSerializer(serializers.ModelSerializer):
    images = NoteImageSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'user', 'links_out', 'links_in', 'images', 'created', 'modified')


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title')