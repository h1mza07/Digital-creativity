# places/views.py
from django.shortcuts import render, redirect

# Fonction pour récupérer tous les lieux (évite la duplication)
def get_all_places():
    """Retourne la liste complète des 24 lieux touristiques du Maroc"""
    return [
        # ============ TANGER ============
        {
            'id': 1,
            'name': 'Kasbah des Musées',
            'city': 'Tanger',
            'description': 'Ancienne résidence des sultans, transformée en musée d\'art marocain avec vue panoramique sur le détroit de Gibraltar.',
            'image_url': 'kasbah_musee.jpg',
            'image_alt': 'Kasbah des Musées à Tanger',
            'lat': 35.788, 
            'lng': -5.812,
            'category': 'Historique',
            'hours': '9h00 - 18h00',
            'price': '20 DH',
            'best_time': 'Avril à Juin',
            'full_description': 'La Kasbah des Musées est une forteresse historique située au point le plus haut de la médina de Tanger. Elle abrite aujourd\'hui le Musée d\'Art Marocain et le Musée des Antiquités. La vue depuis ses remparts sur le détroit de Gibraltar est spectaculaire.'
        },
        {
            'id': 2,
            'name': 'Grottes d\'Hercule',
            'city': 'Tanger',
            'description': 'Grottes naturelles spectaculaires avec une ouverture en forme d\'Afrique sur l\'océan Atlantique.',
            'image_url': 'grottes_hercule.jpg',
            'image_alt': 'Grottes d\'Hercule à Tanger',
            'lat': 35.752, 
            'lng': -5.928,
            'category': 'Naturel',
            'hours': '8h00 - 19h00',
            'price': '10 DH',
            'best_time': 'Toute l\'année',
            'full_description': 'Les Grottes d\'Hercule sont des cavités naturelles creusées par l\'érosion marine. L\'ouverture principale a la forme du continent africain.'
        },
        {
            'id': 3,
            'name': 'Médina de Tanger',
            'city': 'Tanger',
            'description': 'Vieille ville historique aux ruelles étroites, souks animés, et architecture traditionnelle marocaine.',
            'image_url': 'medina_tanger.jpg',
            'image_alt': 'Médina de Tanger',
            'lat': 35.786, 
            'lng': -5.813,
            'category': 'Culturel',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'Matin ou fin d\'après-midi',
            'full_description': 'La médina de Tanger est un labyrinthe de ruelles colorées, de souks animés et de maisons blanches.'
        },
        
        # ============ MARRAKECH ============
        {
            'id': 4,
            'name': 'Place Jemaa el-Fna',
            'city': 'Marrakech',
            'description': 'Place emblématique classée au patrimoine de l\'UNESCO.',
            'image_url': 'jemaa_elfna.jpg',
            'image_alt': 'Place Jemaa el-Fna à Marrakech',
            'lat': 31.626, 
            'lng': -7.989,
            'category': 'Culturel',
            'hours': '24h/24',
            'price': 'Gratuit',
            'best_time': 'En soirée',
            'full_description': 'Cœur battant de Marrakech, cette place historique s\'anime dès le coucher du soleil.'
        },
        {
            'id': 5,
            'name': 'Palais Bahia',
            'city': 'Marrakech',
            'description': 'Chef-d\'œuvre de l\'architecture marocaine du 19ème siècle.',
            'image_url': 'palais_bahia.jpg',
            'image_alt': 'Palais Bahia à Marrakech',
            'lat': 31.619, 
            'lng': -7.973,
            'category': 'Architectural',
            'hours': '9h00 - 17h00',
            'price': '70 DH',
            'best_time': 'Octobre à Avril',
            'full_description': 'Construit à la fin du 19ème siècle, le Palais Bahia compte 150 pièces réparties sur 8 hectares de jardins.'
        },
        {
            'id': 6,
            'name': 'Mosquée Koutoubia',
            'city': 'Marrakech',
            'description': 'Symbole de Marrakech, son minaret du 12ème siècle a inspiré la Giralda de Séville.',
            'image_url': 'mosquee_koutoubia.jpg',
            'image_alt': 'Mosquée Koutoubia à Marrakech',
            'lat': 31.624, 
            'lng': -7.994,
            'category': 'Religieux',
            'hours': 'Extérieur seulement',
            'price': 'Gratuit (extérieur)',
            'best_time': 'Toute la journée',
            'full_description': 'La mosquée Koutoubia, construite sous la dynastie Almohade, est la plus grande mosquée de Marrakech.'
        },
        
        # ============ FÈS ============
        {
            'id': 7,
            'name': 'Médina de Fès el-Bali',
            'city': 'Fès',
            'description': 'Plus grande médina du monde, labyrinthe de 9 400 ruelles classé UNESCO.',
            'image_url': 'medina_fes.jpg',
            'image_alt': 'Médina de Fès',
            'lat': 34.063, 
            'lng': -4.973,
            'category': 'Historique',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'Fondée au 9ème siècle, la médina de Fès est la plus ancienne et la plus grande du monde arabe.'
        },
        {
            'id': 8,
            'name': 'Université Al Quaraouiyine',
            'city': 'Fès',
            'description': 'Plus ancienne université au monde encore en activité, fondée en 859.',
            'image_url': 'al_quaraouiyine.jpg',
            'image_alt': 'Université Al Quaraouiyine',
            'lat': 34.064, 
            'lng': -4.973,
            'category': 'Éducatif',
            'hours': 'Visite guidée seulement',
            'price': 'Non ouvert au public',
            'best_time': 'Sur rendez-vous',
            'full_description': 'Fondée en 859, l\'Université Al Quaraouiyine est la plus ancienne université du monde encore en activité.'
        },
        {
            'id': 9,
            'name': 'Tanneries Chouara',
            'city': 'Fès',
            'description': 'Tanneries traditionnelles utilisant des techniques ancestrales.',
            'image_url': 'tanneries_fes.jpg',
            'image_alt': 'Tanneries Chouara à Fès',
            'lat': 34.065, 
            'lng': -4.980,
            'category': 'Artisanal',
            'hours': '8h00 - 19h00',
            'price': 'Gratuit (vue depuis les terrasses)',
            'best_time': 'Matin',
            'full_description': 'Les tanneries Chouara utilisent des méthodes de tannage du cuir inchangées depuis le Moyen Âge.'
        },
        
        # ============ MEKNÈS ============
        {
            'id': 10,
            'name': 'Bab Mansour',
            'city': 'Meknès',
            'description': 'Porte monumentale considérée comme la plus belle du Maroc.',
            'image_url': 'bab_mansour.jpg',
            'image_alt': 'Bab Mansour à Meknès',
            'lat': 33.894, 
            'lng': -5.565,
            'category': 'Architectural',
            'hours': 'Toujours visible',
            'price': 'Gratuit',
            'best_time': 'Fin d\'après-midi',
            'full_description': 'Construite entre 1672 et 1673, Bab Mansour est la plus grande et plus ornée des portes de Meknès.'
        },
        {
            'id': 11,
            'name': 'Mausolée Moulay Ismail',
            'city': 'Meknès',
            'description': 'Tombeau du sultan Moulay Ismail, fondateur de Meknès.',
            'image_url': 'mausolee_ismail.jpg',
            'image_alt': 'Mausolée Moulay Ismail',
            'lat': 33.892, 
            'lng': -5.563,
            'category': 'Religieux',
            'hours': '9h00 - 12h00, 15h00 - 18h00',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'Ce mausolée abrite la tombe du sultan Moulay Ismail qui régna de 1672 à 1727.'
        },
        {
            'id': 12,
            'name': 'Place El-Hedim',
            'city': 'Meknès',
            'description': 'Grande place animée entre la médina et Bab Mansour.',
            'image_url': 'place_elhedim.jpg',
            'image_alt': 'Place El-Hedim à Meknès',
            'lat': 33.893, 
            'lng': -5.566,
            'category': 'Culturel',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'En soirée',
            'full_description': 'Cette grande place, semblable à la Jamaa el-Fna de Marrakech, est le cœur social de Meknès.'
        },
        
        # ============ RABAT ============
        {
            'id': 13,
            'name': 'Tour Hassan',
            'city': 'Rabat',
            'description': 'Minaret inachevé du 12ème siècle, symbole de Rabat.',
            'image_url': 'tour_hassan.jpg',
            'image_alt': 'Tour Hassan à Rabat',
            'lat': 34.024, 
            'lng': -6.822,
            'category': 'Historique',
            'hours': 'Toujours visible',
            'price': 'Gratuit',
            'best_time': 'Toute la journée',
            'full_description': 'La Tour Hassan est le minaret d\'une mosquée inachevée du 12ème siècle, devenue le symbole de Rabat.'
        },
        {
            'id': 14,
            'name': 'Kasbah des Oudayas',
            'city': 'Rabat',
            'description': 'Forteresse historique avec jardin andalou et vue sur l\'océan.',
            'image_url': 'kasbah_oudayas.jpg',
            'image_alt': 'Kasbah des Oudayas à Rabat',
            'lat': 34.030, 
            'lng': -6.836,
            'category': 'Historique',
            'hours': '8h00 - 20h00',
            'price': 'Gratuit',
            'best_time': 'Après-midi',
            'full_description': 'La Kasbah des Oudayas est une forteresse du 12ème siècle offrant une vue magnifique sur l\'océan Atlantique.'
        },
        {
            'id': 15,
            'name': 'Mausolée Mohammed V',
            'city': 'Rabat',
            'description': 'Tombeau royal d\'architecture marocaine moderne.',
            'image_url': 'mausolee_mohammed5.jpg',
            'image_alt': 'Mausolée Mohammed V à Rabat',
            'lat': 34.023, 
            'lng': -6.823,
            'category': 'Royal',
            'hours': '9h00 - 18h00',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'Ce mausolée abrite les tombes du roi Mohammed V et de ses fils Hassan II et Moulay Abdellah.'
        },
        
        # ============ CASABLANCA ============
        {
            'id': 16,
            'name': 'Mosquée Hassan II',
            'city': 'Casablanca',
            'description': 'Plus grande mosquée d\'Afrique avec minaret de 210 mètres.',
            'image_url': 'hassan2.jpg',
            'image_alt': 'Mosquée Hassan II à Casablanca',
            'lat': 33.607, 
            'lng': -7.632,
            'category': 'Religieux',
            'hours': '9h00 - 17h00 (visites)',
            'price': '120 DH',
            'best_time': 'Matin',
            'full_description': 'La mosquée Hassan II est la plus grande mosquée du Maroc et la 3ème plus grande au monde.'
        },
        {
            'id': 17,
            'name': 'Quartier Habous',
            'city': 'Casablanca',
            'description': 'Quartier historique mélangeant architecture traditionnelle et moderne.',
            'image_url': 'quartier_habous.jpg',
            'image_alt': 'Quartier Habous à Casablanca',
            'lat': 33.573, 
            'lng': -7.632,
            'category': 'Architectural',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'Le quartier Habous, construit dans les années 1930, est un mélange d\'architecture marocaine traditionnelle et moderne.'
        },
        {
            'id': 18,
            'name': 'Cathédrale Sacré-Cœur',
            'city': 'Casablanca',
            'description': 'Ancienne cathédrale de style art déco, maintenant centre culturel.',
            'image_url': 'cathedrale_casablanca.jpg',
            'image_alt': 'Cathédrale Sacré-Cœur à Casablanca',
            'lat': 33.594, 
            'lng': -7.618,
            'category': 'Architectural',
            'hours': 'Extérieur seulement',
            'price': 'Gratuit',
            'best_time': 'Toute la journée',
            'full_description': 'La cathédrale Sacré-Cœur, de style art déco, est un témoignage de l\'histoire coloniale de Casablanca.'
        },
        
        # ============ OUJDA ============
        {
            'id': 19,
            'name': 'Médina d\'Oujda',
            'city': 'Oujda',
            'description': 'Vieille ville historique avec souks traditionnels.',
            'image_url': 'medina_oujda.jpg',
            'image_alt': 'Médina d\'Oujda',
            'lat': 34.681, 
            'lng': -1.908,
            'category': 'Historique',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'La médina d\'Oujda, entourée de remparts, conserve son authenticité avec ses souks traditionnels.'
        },
        {
            'id': 20,
            'name': 'Mosquée Sidi Yahya',
            'city': 'Oujda',
            'description': 'Mosquée historique du 13ème siècle.',
            'image_url': 'sidi_yahya.jpg',
            'image_alt': 'Mosquée Sidi Yahya à Oujda',
            'lat': 34.680, 
            'lng': -1.908,
            'category': 'Religieux',
            'hours': 'Extérieur seulement',
            'price': 'Gratuit',
            'best_time': 'Toute la journée',
            'full_description': 'La mosquée Sidi Yahya, construite au 13ème siècle, est un important centre spirituel d\'Oujda.'
        },
        {
            'id': 21,
            'name': 'Parc Lalla Aïcha',
            'city': 'Oujda',
            'description': 'Jardin public historique au cœur de la ville.',
            'image_url': 'parc_oujda.jpg',
            'image_alt': 'Parc Lalla Aïcha à Oujda',
            'lat': 34.683, 
            'lng': -1.911,
            'category': 'Naturel',
            'hours': '8h00 - 20h00',
            'price': 'Gratuit',
            'best_time': 'Après-midi',
            'full_description': 'Le parc Lalla Aïcha est un jardin public historique offrant un espace de détente au cœur d\'Oujda.'
        },
        
        # ============ AGADIR ============
        {
            'id': 22,
            'name': 'Kasbah d\'Agadir Oufella',
            'city': 'Agadir',
            'description': 'Ruines de la forteresse avec vue sur la baie d\'Agadir.',
            'image_url': 'kasbah_agadir.jpg',
            'image_alt': 'Kasbah d\'Agadir Oufella',
            'lat': 30.433, 
            'lng': -9.615,
            'category': 'Historique',
            'hours': 'Toujours visible',
            'price': 'Gratuit',
            'best_time': 'Coucher de soleil',
            'full_description': 'La Kasbah d\'Agadir Oufella, construite en 1540, offre une vue panoramique exceptionnelle sur la baie d\'Agadir.'
        },
        {
            'id': 23,
            'name': 'Vallée des Oiseaux',
            'city': 'Agadir',
            'description': 'Jardin zoologique avec diverses espèces d\'oiseaux.',
            'image_url': 'vallee_oiseaux.jpg',
            'image_alt': 'Vallée des Oiseaux à Agadir',
            'lat': 30.423, 
            'lng': -9.598,
            'category': 'Naturel',
            'hours': '9h00 - 18h00',
            'price': 'Gratuit',
            'best_time': 'Matin',
            'full_description': 'La Vallée des Oiseaux est un parc zoologique situé en plein centre-ville d\'Agadir.'
        },
        {
            'id': 24,
            'name': 'Marina d\'Agadir',
            'city': 'Agadir',
            'description': 'Port de plaisance moderne avec restaurants et boutiques.',
            'image_url': 'marina_agadir.jpg',
            'image_alt': 'Marina d\'Agadir',
            'lat': 30.416, 
            'lng': -9.619,
            'category': 'Moderne',
            'hours': 'Toute la journée',
            'price': 'Gratuit',
            'best_time': 'En soirée',
            'full_description': 'La marina d\'Agadir est un port de plaisance moderne avec restaurants, boutiques et promenades face à l\'océan.'
        }
    ]

# ============ VUES ============

def place_list(request):
    """Affiche la liste des lieux touristiques avec filtre par ville"""
    places = get_all_places()
    
    # Filtrer par ville si un filtre est spécifié
    city_filter = request.GET.get('city', '')
    if city_filter:
        filtered_places = [p for p in places if p['city'].lower() == city_filter.lower()]
        return render(request, 'places/list.html', {
            'places': filtered_places, 
            'selected_city': city_filter
        })
    
    return render(request, 'places/list.html', {'places': places})

def place_detail(request, place_id):
    """Affiche le détail d'un lieu touristique spécifique"""
    places = get_all_places()
    
    # Trouver le lieu spécifique
    place = None
    for p in places:
        if p['id'] == int(place_id):
            place = p
            break
    
    if not place:
        return redirect('place_list')
    
    return render(request, 'places/detail.html', {'place': place})

def map_view(request):
    """Affiche la carte interactive avec tous les lieux géolocalisés"""
    places = get_all_places()
    
    # Préparer les données pour la carte
    map_data = {
        'places': places,
        'total_places': len(places),
        'cities_count': len(set(p['city'] for p in places))  # Nombre de villes uniques
    }
    
    return render(request, 'places/map_view.html', map_data)