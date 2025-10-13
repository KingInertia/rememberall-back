from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Note (TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='notes')
    links_out = models.ManyToManyField('self', symmetrical=False, related_name='links_in', blank=True)


class NoteImage (models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='note_images/')

    def __str__(self):
        return f"Image for Note: {self.note.title}"
