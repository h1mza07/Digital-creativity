# routes/admin.py
from django.contrib import admin
from .models import Itinerary, Route, CustomItinerary, ItineraryStop

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'hotel', 'stadium', 'city', 'difficulty', 'created_by', 'created_at']
    list_filter = ['city', 'difficulty', 'created_at']
    search_fields = ['title', 'city', 'hotel_name', 'stadium_name']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'duration_days', 'difficulty', 'city', 'image')
        }),
        ('Hôtel', {
            'fields': ('hotel', 'hotel_name', 'hotel_rating', 'hotel_price', 'hotel_address')
        }),
        ('Stade', {
            'fields': ('stadium', 'stadium_name', 'stadium_address', 'distance')
        }),
        ('Informations pratiques', {
            'fields': ('best_season', 'required_equipment', 'contact_info', 'total_price')
        }),
        ('Métadonnées', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'hotel', 'stadium', 'distance_km', 'transport_mode', 'price_estimate']
    list_filter = ['transport_mode', 'hotel']
    search_fields = ['name', 'hotel__name', 'stadium__name']


@admin.register(CustomItinerary)
class CustomItineraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'is_public', 'views_count']
    list_filter = ['is_public', 'created_at']
    search_fields = ['title', 'user__username']


@admin.register(ItineraryStop)
class ItineraryStopAdmin(admin.ModelAdmin):
    list_display = ['itinerary', 'order', 'get_display_name', 'get_display_type']
    list_filter = ['itinerary']
    search_fields = ['itinerary__title']
    
    def get_display_name(self, obj):
        """Retourne le nom affichable de l'étape"""
        if obj.place:
            return obj.place.name
        elif obj.hotel:
            return obj.hotel.name
        elif obj.city:
            return obj.city.name
        return "Étape inconnue"
    get_display_name.short_description = 'Nom'
    
    def get_display_type(self, obj):
        """Retourne le type affichable de l'étape"""
        if obj.place:
            return 'Lieu touristique'
        elif obj.hotel:
            return 'Hôtel'
        elif obj.city:
            return 'Ville'
        return 'Inconnu'
    get_display_type.short_description = 'Type'