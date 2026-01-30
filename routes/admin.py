from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'stadium_name', 'city', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('hotel_name', 'stadium_name')
    filter_horizontal = ('cities',)  