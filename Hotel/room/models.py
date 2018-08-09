from django.db import models

# Create your models here.


class Room(models.Model):

    # photos = models.ImageField()
    room_nmb = models.IntegerField()
    room_size = models.IntegerField()
    number_of_beds = models.IntegerField()
    # Djangowy
    # model
    # przedstawiajacy
    # Room
    # w
    # bazie
    # danych
    # ma
    # miec
    # informacje
    # o
    # nr
    # pokoju, jego
    # wielkosc(zwykly
    # int) i
    # ilość
    # łóżek.
