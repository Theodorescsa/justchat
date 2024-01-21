# views.py
from django.shortcuts import render
from .models import RoomModel, MessageModel
from .consumers import ChatConsumer
x = ChatConsumer.chat_message
def index(request): 

    return render(request, "chat/index.html")

 
def room(request, room_name):
    name = room_name
    model, created = RoomModel.objects.get_or_create(
            name = name
        )
    # room_model = RoomModel.objects.get(name = room_name)
    # message_model, created = MessageModel.objects.get_or_create(
    #     room_name = room_model,
    #     message = ????
    # ) 
    return render(request, "chat/room.html", {"room_name": room_name})
