 # places/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans la liste admin
    list_display = ('name', 'city', 'category', 'display_image', 'created_at', 'updated_at')
    
    # Filtres par côté droit
    list_filter = ('city', 'category', 'created_at')
    
    # Barre de recherche
    search_fields = ('name', 'description', 'city__name', 'address')
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'city', 'category', 'description')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude', 'address')
        }),
        ('Médias', {
            'fields': ('image',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    # Champs en lecture seule
    readonly_fields = ('created_at', 'updated_at', 'display_image')
    
    # Organisation par défaut
    ordering = ('-created_at', 'name')
    
    # Nombre d'éléments par page
    list_per_page = 25
    
    # Prévisualisation des relations
    autocomplete_fields = ['city']
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
        return "Pas d'image"
    display_image.short_description = 'Image'
    
    # Actions personnalisées
    actions = ['mark_as_popular']
    
    def mark_as_popular(modeladmin, request, queryset):
        queryset.update(category='monument')
        modeladmin.message_user(request, f"{queryset.count()} lieux marqués comme monuments.")
    mark_as_popular.short_description = "Marquer comme monument"