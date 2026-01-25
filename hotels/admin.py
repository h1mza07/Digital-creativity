# hotels/admin.py
from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating', 'price')
    list_filter = ('city', 'rating')
    search_fields = ('name', 'description')