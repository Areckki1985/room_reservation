from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    # model responsible for room for rental

    name = models.CharField(max_length=255)
    description = models.TextField()
    for_how_many_people = models.SmallIntegerField()
    how_many_seated = models.SmallIntegerField(null=True)
    space = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.name)

class RoomImages(models.Model):
    # model responsible for storing room images

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

class RentedRoomsList(models.Model):
    # model storing information about unavailable rooms

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rental_from = models.DateField()
    rental_up_to = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class AdditionalStuff(models.Model):
    # model responsible for additional stuff, that can be added to room rental

    name = models.CharField(max_length=255)
    quantity = models.SmallIntegerField(default=1)
    description = models.TextField()

class RentedAdditionalStuffList(models.Model):
    # model storing information about unavailable additional stuff

    stuff = models.ForeignKey(AdditionalStuff, on_delete=models.CASCADE)
    rental_from = models.DateField()
    rental_up_to = models.DateField()
    quantity = models.SmallIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
