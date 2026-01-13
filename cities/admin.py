from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')