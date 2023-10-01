from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
# Create your views here.
@login_required
def Rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms':rooms})

@login_required
def Room_detail(request,slug):
    room_detail = Room.objects.get(slug=slug)
    return render(request, "rooms/room_detail.html", {'room_detail': room_detail})

def room_delete(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_detail')  # Redirect to your desired page after deletion
    return render(request, 'rooms/room_delete.html', {'room': room})