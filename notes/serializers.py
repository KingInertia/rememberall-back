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
        fields = ('id', 'title', 'content', 'links_out', 'links_in', 'images')


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title')