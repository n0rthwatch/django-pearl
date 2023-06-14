from django.contrib import admin

from rooms.forms import RoomForm
from rooms.models import *


class RoomImageInline(admin.TabularInline):
    model = RoomImage


class ServiceInline(admin.TabularInline):
    model = Room.services.through


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline, ServiceInline]
    list_display = ['title', 'category', 'max_adults', 'max_children', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    form = RoomForm


@admin.register(RoomImage)
class RoomImagesAdmin(admin.ModelAdmin):
    model = RoomImage
    list_display = ['image_tag', 'room']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ['name', 'position', 'main']
    search_fields = ['name', 'position']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ['room', 'check_in', 'check_out', 'adult_count', 'child_count']
    list_filter = ['room', 'check_in', 'check_out']
