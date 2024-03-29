from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RoomModel(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now = True,null=True )
    def __str__(self):
        return self.name

class MessageModel(models.Model):
    user = models.ForeignKey(User,on_delete = models.PROTECT, null = True)
    room_name = models.ForeignKey(RoomModel,on_delete = models.PROTECT)
    message = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.message