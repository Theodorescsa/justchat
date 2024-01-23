# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MessageModel, RoomModel
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]
        # Attempt to save the message to the database
        try:
            await Save_Messages(message, self.room_name, user)
        except Exception as e:
            print(f"Error saving message to database: {e}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

@database_sync_to_async
def Save_Messages(message, room_name, user):
    # Retrieve or create RoomModel instance based on the room name
    room_instance, created = RoomModel.objects.get_or_create(name=room_name)
    # Create MessageModel instance with the correct room instance
    return MessageModel.objects.create(message=message, room_name=room_instance, user=user)
