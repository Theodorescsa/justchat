# views.py
from django.shortcuts import render
from .models import RoomModel, MessageModel
from .consumers import ChatConsumer
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
@login_required(login_url=settings.LOGIN_URL)
def index(request): 

    return render(request, "chat/index.html")

@login_required(login_url=settings.LOGIN_URL)
def room(request, room_name):
    name = room_name
    model, created = RoomModel.objects.get_or_create(
            name = name,
            
        )
    messages = MessageModel.objects.all()
    context = {
        'messages':messages,
        "room_name": room_name,
    }
    return render(request, "chat/room.html",context)
