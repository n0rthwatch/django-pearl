from django.urls import path
from rooms.views import *

app_name = 'rooms'

urlpatterns = [
    path('check_availability/', check_availability, name='check_availability'),
    path('book_room/', book_room, name='book_room'),
    path('booking_success/', booking_success, name='booking_success'),
    path('room_info/<int:room_id>/', room_info, name='room_info'),
    path('', RoomListView.as_view(), name='room_list'),
    path('<slug:room_slug>/', RoomDetailView.as_view(), name='room_detail'),
]
