from django.db import models
from datetime import datetime
import django.utils


class Settings(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Room(models.Model):
    # Get the next free number in the ordering
    def number():
        no = Room.objects.all().count()
        if no == None:
            return 1
        else:
            return no + 1

    friendly_name = models.CharField(max_length=30)
    displayOrder = models.IntegerField(default=number)


class NSPanel(models.Model):
    mac_address = models.CharField(max_length=17)
    friendly_name = models.CharField(max_length=100)
    last_seen = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.CharField(max_length=15, default="")
    version = models.CharField(max_length=15, default="")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Light(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    friendly_name = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=16, default="manual") # "home_assistant", "openhab" or "manual"
    is_ceiling_light = models.BooleanField(default=False)
    can_dim = models.BooleanField(default=False)
    can_rgb = models.BooleanField(default=False)
    can_color_temperature = models.BooleanField(default=False)
