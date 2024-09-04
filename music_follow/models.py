# myapp/models.py

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    telephone = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add =True, null=True)
    

    def __str__(self):
        return self.user.username


# for live streaming
from django.db import models
from django.contrib.auth.models import User

class LiveSession(models.Model):
    title = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_live = models.BooleanField(default=False)

class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    live_session = models.ForeignKey(LiveSession, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    live_session = models.ForeignKey(LiveSession, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=50)  # e.g., 'like', 'laugh', etc.
    created_at = models.DateTimeField(auto_now_add=True)
    
