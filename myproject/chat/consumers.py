from channels.consumer import AsyncConsumer
from django.conf import settings
from .models import Message
import json
import datetime

'''class UserNotification(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("gossip", self.channel_name)

	async def disconnect(self):
		await self.channel_layer.group_discard("gossip", self.channel_name)

	async def user_gossip(self, event):
		await self.send_json(event)'''

class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		print ("connected", event)
		
		await self.send({
			"type": "websocket.accept"
		})

		await self.send({
			"type": "websocket.send",
		})
		 
	async def websocket_disconnect(self, event):
		print ("disconnected", event)

	async def websocket_receive(self, event):
		print ("receive", event)
		front_text = event.get('text', None)
		if front_text is not None:
			loaded_dict_data = json.loads(front_text)
			msg = loaded_dict_data.get('message')
			user = self.scope['user']
			username = 'default'
			if user.is_authenticated:
				username = user.username
			myResponse = {
				'message': msg,
				'username': username
			}
			await self.send({
				"type": "websocket.send",
				"text": json.dumps(myResponse)
			})