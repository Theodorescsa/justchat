# Generated by Django 4.2.6 on 2024-01-21 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_roomdetailmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomDetailModel',
        ),
    ]