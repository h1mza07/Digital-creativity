from django.shortcuts import render, get_object_or_404
from .models import Place
from cities.models import City

def places_list(request):
    """Affiche TOUS les lieux touristiques"""
    places = Place.objects.all().select_related('city')
    context = {
        'places': places,
        'title': 'Tous les lieux touristiques'
    }
    return render(request, 'places/places_list.html', context)

def place_detail(request, id):
    """Affiche le détail d'un lieu spécifique"""
    place = get_object_or_404(Place.objects.select_related('city'), id=id)
    context = {
        'place': place,
        'title': f'{place.name} - {place.city.name}'
    }
    return render(request, 'places/place_detail.html', context)

def city_places(request, city_id):
    """Affiche les lieux d'une VILLE spécifique"""
    city = get_object_or_404(City, id=city_id)
    places = city.places.all()
    context = {
        'city': city,
        'places': places,
        'title': f'Lieux touristiques à {city.name}'
    }
    return render(request, 'places/city_places.html', context)