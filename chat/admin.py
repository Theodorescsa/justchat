from django.contrib import admin
from .models import RoomModel, MessageModel
# Register your models here.
admin.site.register(RoomModel)
admin.site.register(MessageModel)

