# places/admin.py
from django.contrib import admin
from .models import Stadium, Place

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'capacity', 'is_world_cup_venue']
    list_filter = ['city', 'is_world_cup_venue']
    search_fields = ['name', 'city__name']
    readonly_fields = ['created_at'] if hasattr(Stadium, 'created_at') else []


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'place_type', 'is_free']
    list_filter = ['city', 'place_type', 'is_free']
    search_fields = ['name', 'city__name', 'description']
    ordering = ['name']