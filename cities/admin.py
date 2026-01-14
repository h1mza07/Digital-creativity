from django.contrib import admin
from .models import City, TouristPlace 

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TouristPlace) 
class TouristPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'type', 'created_at')
    list_filter = ('type', 'city', 'created_at')
    search_fields = ('name', 'description', 'city__name')
    readonly_fields = ('created_at', 'updated_at')