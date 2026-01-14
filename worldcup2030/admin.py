from django.contrib import admin
from .models import HostCity

@admin.register(HostCity)
class HostCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'is_host', 'stadium_capacity', 'matches_count')
    list_filter = ('is_host', 'created_at')
    search_fields = ('city__name', 'infrastructure_details')
    readonly_fields = ('created_at', 'updated_at')