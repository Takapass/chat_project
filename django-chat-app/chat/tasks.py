from celery import shared_task
from django.utils import timezone
from .models import ChatRoom, User
import random

@shared_task
def create_chat_room():
    # 新しいトークルームを作成
    room = ChatRoom.objects.create(created_at=timezone.now())
    assign_users_to_room(room)

@shared_task
def delete_old_rooms():
    # 古いトークルームを削除
    expiration_time = timezone.now() - timezone.timedelta(days=1)
    ChatRoom.objects.filter(created_at__lt=expiration_time).delete()

def assign_users_to_room(room):
    # ユーザーをランダムにトークルームに割り振る
    users = list(User.objects.all())
    random_users = random.sample(users, min(len(users), 10))  # 最大10人を割り振る
    for user in random_users:
        room.users.add(user)  # トークルームにユーザーを追加

    room.save()