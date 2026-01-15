from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    # Affichage dans la liste
    list_display = ('name', 'city', 'category', 'entry_price', 'is_featured')
    list_filter = ('city', 'category', 'is_featured')
    search_fields = ('name', 'description', 'city__name')
    
    # Organisation des champs
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'city', 'category', 'description')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude')
        }),
        ('Prix et horaires', {
            'fields': ('entry_price', 'opening_hours', 'best_time_to_visit'),
            'classes': ('collapse',)
        }),
        ('Image', {
            'fields': ('main_image',)
        }),
        ('Options', {
            'fields': ('is_featured',)
        }),
    )
