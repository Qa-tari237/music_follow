# myapp/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("artist", "Artist"),
        ("subscriber", "Subscriber")
    ]
    STATUS_CHOICES = [
        ("pending", "PENDING"),
        ("active", "ACTIVE"),
        ("inactive", "INACTIVE")
    ]
    tel = models.CharField(max_length=25, unique=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="pending")
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default="subscriber")


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')


class LiveSession(models.Model):
    title = models.CharField(max_length=200)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_live = models.BooleanField(default=False)


class Subscriber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    live_session = models.ForeignKey(LiveSession, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    live_session = models.ForeignKey(LiveSession, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=50)  # e.g., 'like', 'laugh', etc.
    created_at = models.DateTimeField(auto_now_add=True)
    