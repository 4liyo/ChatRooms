from django.urls import path
from . import views

urlpatterns = [
    path('', views.Rooms, name='rooms'),
    path('<slug:slug>/', views.Room_detail, name='room_detail'),


]