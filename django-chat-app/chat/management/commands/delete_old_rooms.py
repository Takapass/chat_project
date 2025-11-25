from django.core.management.base import BaseCommand
from django.utils import timezone
from chat.models import ChatRoom  # Assuming you have a ChatRoom model

class Command(BaseCommand):
    help = 'Delete old chat rooms'

    def handle(self, *args, **kwargs):
        # Get the current time
        now = timezone.now()
        # Define the threshold for old rooms (e.g., older than 24 hours)
        threshold = now - timezone.timedelta(days=1)
        
        # Delete chat rooms older than the threshold
        old_rooms = ChatRoom.objects.filter(created_at__lt=threshold)
        deleted_count, _ = old_rooms.delete()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} old chat rooms.'))