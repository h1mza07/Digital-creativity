# routes/admin.py
from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'duration_days', 'difficulty', 'created_by', 'created_at']
    list_filter = ['city', 'difficulty', 'created_at']
    search_fields = ['title', 'city', 'hotel_name', 'stadium_name']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'duration_days', 'difficulty', 'city', 'image')
        }),
        ('Hôtel', {
            'fields': ('hotel_name', 'hotel_rating', 'hotel_price', 'hotel_address')
        }),
        ('Stade', {
            'fields': ('stadium_name', 'stadium_address', 'distance')
        }),
        ('Informations pratiques', {
            'fields': ('best_season', 'required_equipment', 'contact_info', 'total_price')
        }),
        ('Métadonnées', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )