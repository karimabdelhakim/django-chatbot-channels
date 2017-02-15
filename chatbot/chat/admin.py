from django.contrib import admin

from .models import ChatMessage
# Register your models here.

class ChatMessageModelAdmin(admin.ModelAdmin):
	list_display = ["message","timestamp","id"]
	list_display_links = ["timestamp"]
	list_filter = ["timestamp"]
	ordering = ['timestamp']
	class Meta:
		model = ChatMessage


admin.site.register(ChatMessage, ChatMessageModelAdmin)