from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_days', 'difficulty', 'rating', 'views_count')
    list_filter = ('difficulty', 'rating')
    search_fields = ('name', 'description')
    filter_horizontal = ('cities',)  