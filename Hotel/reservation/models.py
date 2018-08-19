from django.db import models
from django.contrib.auth.models import User
from room.models import Room

# Create your models here.


class Reservation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.user',  related_name='reservations', on_delete=models.CASCADE)
    res_room = models.ForeignKey(Room, related_name='reservations', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('created', )

