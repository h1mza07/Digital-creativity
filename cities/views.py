# cities/views.py - VERSION FINALE
from django.shortcuts import render, get_object_or_404
from .models import City

def city_list(request):
    """Liste des villes"""
    cities = City.objects.all()
    return render(request, 'cities/list.html', {
        'cities': cities,
        'page_title': 'Villes Marocaines - Maroc Tourisme 2030'
    })

def city_detail(request, slug):
    """Détail d'une ville"""
    city = get_object_or_404(City, slug=slug)
    return render(request, 'cities/detail.html', {
        'city': city,
        'page_title': f'{city.name} - Maroc Tourisme 2030'
    })