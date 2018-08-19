from django.db import models

# Create your models here.


class Room(models.Model):

    room_nmb = models.IntegerField()
    room_size = models.IntegerField()
    number_of_beds = models.IntegerField()
