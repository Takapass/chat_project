from django.db import models
from django.contrib.auth.models import User
import random

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class RoomUser(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} in {self.chat_room.name}"

def assign_users_to_rooms():
    chat_rooms = ChatRoom.objects.all()
    users = User.objects.all()
    for room in chat_rooms:
        room_users = random.sample(list(users), min(len(users), 5))  # Assign up to 5 random users
        for user in room_users:
            RoomUser.objects.get_or_create(chat_room=room, user=user)