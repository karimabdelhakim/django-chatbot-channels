from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class ChatMessage(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	message = models.CharField(max_length=255)
	owner = models.TextField(max_length=4)
	timestamp = models.DateTimeField(auto_now_add=True)

	@property
	def formatted_timestamp(self):
		return self.timestamp.strftime('%b %-d %-I:%M %p')