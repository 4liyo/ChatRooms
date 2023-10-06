from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
# Create your views here.
@login_required
def Rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms':rooms})

@login_required
def Room_detail(request,slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, "rooms/room_detail.html", {'room': room,'messages': messages})

