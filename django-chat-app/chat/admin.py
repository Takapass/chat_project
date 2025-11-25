from django.contrib import admin
from .models import UserProfile, ChatRoom

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'created_at')
    search_fields = ('user__username',)

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    search_fields = ('name',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)