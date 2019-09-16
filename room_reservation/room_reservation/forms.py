from django.forms import ModelForm

from room_reservation.models import Room, RoomImages

class Room(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'for_how_many_people', 'how_many_seated', 'space']

class RoomImages(ModelForm):
    class Meta:
        model = RoomImages
        fields = ['image']
