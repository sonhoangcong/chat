from django.urls import path
from . import consumers

websocket_urlpatterns = [
	path('chat/index/', consumers.ChatConsumer),
]