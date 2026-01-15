from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Place
from cities.models import City

class PlaceListView(ListView):
    """Vue pour afficher la liste des lieux touristiques"""
    model = Place
    template_name = 'places/list.html'
    context_object_name = 'places'
    paginate_by = 6
    
    def get_queryset(self):
        """Filtrage des lieux selon les paramètres GET"""
        queryset = Place.objects.all().select_related('city')
        
        # Récupération des paramètres de filtre
        city_id = self.request.GET.get('city')
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        
        # Application des filtres
        if city_id and city_id != 'all':
            queryset = queryset.filter(city_id=city_id)
        
        if category and category != 'all':
            queryset = queryset.filter(category=category)
        
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(city__name__icontains=search)
            )
        
        return queryset.order_by('name')
    
    def get_context_data(self, **kwargs):
        """Ajout des données de contexte pour les filtres"""
        context = super().get_context_data(**kwargs)
        
        # Liste des villes pour le filtre
        context['cities'] = City.objects.all().order_by('name')
        
        # Liste des catégories disponibles
        context['categories'] = Place.CATEGORY_CHOICES
        
        # Récupération des valeurs actuelles des filtres
        context['selected_city'] = self.request.GET.get('city', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['search_query'] = self.request.GET.get('search', '')
        
        return context


class PlaceDetailView(DetailView):
    """Vue pour afficher le détail d'un lieu touristique"""
    model = Place
    template_name = 'places/detail.html'
    context_object_name = 'place'
    
    def get_context_data(self, **kwargs):
        """Ajout des données de contexte pour la carte et les lieux similaires"""
        context = super().get_context_data(**kwargs)
        
        # Données pour la carte Leaflet
        place = self.object
        context['map_center'] = {
            'lat': place.latitude if place.latitude else 31.7917,
            'lng': place.longitude if place.longitude else -7.0926
        }
        
        # Récupération des lieux similaires (même ville ou même catégorie)
        similar_places = Place.objects.filter(
            Q(city=place.city) | Q(category=place.category)
        ).exclude(id=place.id)[:4]
        
        context['similar_places'] = similar_places
        
        # Données structurées pour les cartes
        context['places_data'] = [
            {
                'name': place.name,
                'lat': place.latitude,
                'lng': place.longitude,
                'category': place.category,
                'url': place.get_absolute_url() if hasattr(place, 'get_absolute_url') else '#'
            }
            for place in Place.objects.all() if place.latitude and place.longitude
        ]
        
        return context


def place_map_view(request):
    """Vue pour la carte interactive de tous les lieux"""
    places = Place.objects.filter(
        latitude__isnull=False, 
        longitude__isnull=False
    )
    
    # Préparation des données pour Leaflet
    places_data = []
    for place in places:
        places_data.append({
            'id': place.id,
            'name': place.name,
            'lat': float(place.latitude),
            'lng': float(place.longitude),
            'category': place.category,
            'city': place.city.name if place.city else '',
            'description': place.description[:100] + '...' if len(place.description) > 100 else place.description,
            'image_url': place.main_image.url if place.main_image else ''
        })
    
    context = {
        'places': places,
        'places_data': places_data,
        'map_center': {'lat': 31.7917, 'lng': -7.0926},  # Centre sur le Maroc
    }
    
    return render(request, 'places/map.html', context)


def place_by_city_view(request, city_id):
    """Vue pour afficher les lieux d'une ville spécifique"""
    city = get_object_or_404(City, id=city_id)
    places = Place.objects.filter(city=city).select_related('city')
    
    context = {
        'city': city,
        'places': places,
        'total_places': places.count(),
    }
    
    return render(request, 'places/city_places.html', context)
