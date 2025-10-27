from django.contrib.auth import get_user_model
from .models import Note, NoteHistory
from users.models import User

def update_note_history(user: User, note: Note) -> None:
    NoteHistory.objects.filter(user=user, note=note).delete()
    NoteHistory.objects.create(user=user, note=note)
    max_items = 8

    history = NoteHistory.objects.filter(user=user)
    if history.count() > max_items:
        for old_n in history[max_items:]:
            old_n.delete()
