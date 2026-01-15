from django.contrib import admin
from .models import HostCity, Stadium  # ← AJOUTER Stadium

@admin.register(HostCity)
class HostCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'is_host', 'stadium_capacity', 'matches_count')
    list_filter = ('is_host', 'created_at')
    search_fields = ('city__name', 'infrastructure_details')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Stadium)  # ← NOUVELLE CLASSE
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'host_city', 'capacity', 'construction_year')
    list_filter = ('construction_year', 'host_city')
    search_fields = ('name', 'description', 'address')
    readonly_fields = ('created_at', 'updated_at')