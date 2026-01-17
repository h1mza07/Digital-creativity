from django.shortcuts import render, get_object_or_404
from .models import Itinerary

def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'routes/itinerary_list.html', {'itineraries': itineraries})

def itinerary_detail(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    return render(request, 'routes/itinerary_detail.html', {'itinerary': itinerary})
    def profile_view(request):
    return render(request, 'profile.html')

def about(request):
    """
    Page 'À propos' présentant les 4 membres de l'équipe.
    """
    team_members = [
        {
            'name': 'Hamza Layachi',
            'role': 'Chef de projet & Core Backend',
            'responsibilities': [
                'Initialisation du projet Django',
                'Configuration globale (settings.py, urls.py)',
                'Création des apps: cities, worldcup2030',
                'Modèles: City, HostCity, Stadium',
                'Page d’accueil et structure globale des templates'
            ]
        },
        {
            'name': 'Ainzura IBtissam',
            'role': 'Lieux touristiques & Cartographie',
            'responsibilities': [
                'App: places',
                'Modèle: Place + relations avec City',
                'Intégration Leaflet (cartes interactives)',
                'Templates: liste et détail des lieux'
            ]
        },
        {
            'name': 'EL Assioui Imane',
            'role': 'Hôtels & Itinéraires',
            'responsibilities': [
                'Apps: hotels, routes',
                'Modèles: Hotel, Itinerary',
                'Relations: Hotel → City, Itinerary → Cities',
                'Templates: hôtels, détails itinéraires, cartes de parcours'
            ]
        },
        {
            'name': 'Amina Chetti',
            'role': 'Utilisateurs, Sécurité & UX',
            'responsibilities': [
                'App: users',
                'Authentification (inscription, connexion)',
                'Modèles: Profile, Favoris',
                'Sécurité (CSRF, login_required)',
                'UX: formulaires, messages, accessibilité'
            ]
        }
    ]
    return render(request, 'routes/about.html', {'team_members': team_members})