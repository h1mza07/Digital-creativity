from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'description', 'city__name')
    ordering = ('-created_at',)
    list_per_page = 20
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'city', 'description')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude')
        }),
        ('Image', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )