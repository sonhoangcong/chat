from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
	list_display = ['user','group_name', 'message', 'created']

admin.site.register(Message, MessageAdmin)