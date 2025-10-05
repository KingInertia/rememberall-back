from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class User (AbstractUser, TimeStampedModel):
    image_path = models.ImageField(upload_to='user_images/', null=True, blank=True)