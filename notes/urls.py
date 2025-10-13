from rest_framework.routers import DefaultRouter

from .views import NoteViewSet, NoteImageViewSet

router = DefaultRouter()

router.register(r'notes', NoteViewSet, basename='note')
router.register(r'note-images', NoteImageViewSet, basename='noteimage')