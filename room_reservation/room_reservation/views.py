from django.shortcuts import render

from room_reservation.forms import Room, RoomImages

from django.views import View
from django.http import HttpResponseRedirect
from room_reservation.service import RoomService

class CreateRoomView(View):
    # View that allows authenticated users to add rooms prepared for rental

    def get(self, request):
        form = Room
        form2 = RoomImages

        return render(request, 'add_room.html', {'form':form, 'form2':form2})

    def post(self, request):
        form = Room(request.POST)
        form2 = RoomImages(request.POST, request.FILES)
        room_service = RoomService(request.user)

        if form.is_valid() and form2.is_valid() and request.user.is_authenticated:
            room_service.add_new_room(form, form2)
            return HttpResponseRedirect('')
        elif form.is_valid() and form2.is_valid():
            message = room_service.FAILED_USER_AUTHENTICATION
            return render(request, 'add_room.html', {'form': form, 'form2':form2, 'message': message})
        else:
            message = room_service.FAILED_CREATION_MESSAGE
            return render(request, 'add_room.html', {'form': form, 'form2':form2, 'message': message})

