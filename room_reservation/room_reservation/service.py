from room_reservation.models import Room, RoomImages, RentedRoomsList, AdditionalStuff, RentedAdditionalStuffList

class RoomService:
    SUCCESS_CREATION_MESSAGE = 'Nowa sala została dodana'
    FAILED_CREATION_MESSAGE = 'Wypełnij poprawnie wszystkie pola'
    FAILED_USER_AUTHENTICATION = 'Aby dodać sale musisz być zalogowany'

    def __init__(self, user):
        self.user = user

    def add_new_room(self, validated_form, validated_form2):
        room = validated_form.save(commit=False)
        image = validated_form2.save(commit=False)
        room.save()
        image.room_id = room.id
        image.save()

