# places/create_sample_places.py
import os
import django
import sys

# Configure Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from places.models import Place
from cities.models import City

# Données des lieux touristiques par ville
TOURISTIC_PLACES = {
    'Marrakech': [
        {
            'name': 'Jardin Majorelle',
            'description': 'Jardin botanique créé par le peintre Jacques Majorelle, célèbre pour son bleu intense.',
            'category': 'jardin',
            'latitude': 31.6412,
            'longitude': -8.0014,
            'address': 'Rue Yves Saint Laurent, Marrakech',
            'entry_price': 70.00,
            'opening_hours': '8h00 - 17h30',
            'best_time_to_visit': 'Printemps et automne'
        },
        {
            'name': 'Place Jemaa el-Fna',
            'description': 'Place emblématique classée au patrimoine mondial de l\'UNESCO, animation jour et nuit.',
            'category': 'monument',
            'latitude': 31.6258,
            'longitude': -7.9891,
            'address': 'Medina, Marrakech',
            'entry_price': 0.00,
            'opening_hours': '24h/24',
            'best_time_to_visit': 'Soirée pour l\'ambiance'
        },
        {
            'name': 'Palais de la Bahia',
            'description': 'Palais du XIXe siècle avec jardins, fontaines et décors traditionnels marocains.',
            'category': 'monument',
            'latitude': 31.6192,
            'longitude': -7.9776,
            'address': 'Rue Riad Zitoun el Jdid, Marrakech',
            'entry_price': 70.00,
            'opening_hours': '9h00 - 16h30',
            'best_time_to_visit': 'Matin pour éviter la foule'
        },
    ],
    'Fès': [
        {
            'name': 'Medina de Fès el-Bali',
            'description': 'Plus vieille médina du Maroc, classée patrimoine mondial de l\'UNESCO.',
            'category': 'monument',
            'latitude': 34.0626,
            'longitude': -4.9730,
            'address': 'Fès el-Bali, Fès',
            'entry_price': 0.00,
            'opening_hours': 'Toute la journée',
            'best_time_to_visit': 'Toute l\'année'
        },
        {
            'name': 'Université Al Quaraouiyine',
            'description': 'Plus ancienne université du monde encore en activité, fondée en 859.',
            'category': 'mosquee',
            'latitude': 34.0646,
            'longitude': -4.9738,
            'address': 'Fès el-Bali, Fès',
            'entry_price': 0.00,
            'opening_hours': 'Hors prières',
            'best_time_to_visit': 'Matin'
        },
    ],
    'Casablanca': [
        {
            'name': 'Mosquée Hassan II',
            'description': 'Plus grande mosquée d\'Afrique, avec minaret de 210 mètres au bord de l\'océan.',
            'category': 'mosquee',
            'latitude': 33.6085,
            'longitude': -7.6326,
            'address': 'Boulevard de la Corniche, Casablanca',
            'entry_price': 130.00,
            'opening_hours': '9h00 - 14h00 (visites guidées)',
            'best_time_to_visit': 'Matin pour la lumière'
        },
        {
            'name': 'Corniche de Casablanca',
            'description': 'Promenade au bord de l\'océan Atlantique avec restaurants et plages.',
            'category': 'plage',
            'latitude': 33.5961,
            'longitude': -7.6320,
            'address': 'Ain Diab, Casablanca',
            'entry_price': 0.00,
            'opening_hours': '24h/24',
            'best_time_to_visit': 'Coucher de soleil'
        },
    ],
    'Rabat': [
        {
            'name': 'Tour Hassan',
            'description': 'Minaret inachevé de la mosquée Hassan, symbole de Rabat.',
            'category': 'monument',
            'latitude': 34.0242,
            'longitude': -6.8227,
            'address': 'Boulevard Mohamed Lyazidi, Rabat',
            'entry_price': 0.00,
            'opening_hours': '8h00 - 18h00',
            'best_time_to_visit': 'Fin d\'après-midi'
        },
        {
            'name': 'Kasbah des Oudayas',
            'description': 'Forteresse historique avec vue sur l\'océan et rues bleu et blanc.',
            'category': 'kasbah',
            'latitude': 34.0285,
            'longitude': -6.8368,
            'address': 'Rue des Consuls, Rabat',
            'entry_price': 0.00,
            'opening_hours': '8h00 - 18h00',
            'best_time_to_visit': 'Matin'
        },
    ],
    'Tanger': [
        {
            'name': 'Grottes d\'Hercule',
            'description': 'Grottes naturelles avec ouverture sur la mer, liée au mythe d\'Hercule.',
            'category': 'nature',
            'latitude': 35.7923,
            'longitude': -5.5576,
            'address': 'Cap Spartel, Tanger',
            'entry_price': 10.00,
            'opening_hours': '9h00 - 19h00',
            'best_time_to_visit': 'Marée basse'
        },
        {
            'name': 'Kasbah de Tanger',
            'description': 'Ancienne forteresse avec musée et vue sur le détroit de Gibraltar.',
            'category': 'kasbah',
            'latitude': 35.7884,
            'longitude': -5.8129,
            'address': 'Place de la Kasbah, Tanger',
            'entry_price': 20.00,
            'opening_hours': '9h00 - 18h00',
            'best_time_to_visit': 'Après-midi'
        },
    ],
    'Agadir': [
        {
            'name': 'Plage d\'Agadir',
            'description': 'Une des plus belles plages du Maroc, sable fin et climat doux toute l\'année.',
            'category': 'plage',
            'latitude': 30.4167,
            'longitude': -9.5833,
            'address': 'Corniche d\'Agadir',
            'entry_price': 0.00,
            'opening_hours': '24h/24',
            'best_time_to_visit': 'Été'
        },
        {
            'name': 'Vallée des Oiseaux',
            'description': 'Parc zoologique gratuit avec animaux locaux et jardin botanique.',
            'category': 'nature',
            'latitude': 30.4265,
            'longitude': -9.5960,
            'address': 'Boulevard du 20 Août, Agadir',
            'entry_price': 0.00,
            'opening_hours': '9h00 - 18h00',
            'best_time_to_visit': 'Matin'
        },
    ],
    'Meknès': [
        {
            'name': 'Place El Hedim',
            'description': 'Place principale de Meknès avec arcades, marchés et animations.',
            'category': 'souk',
            'latitude': 33.8935,
            'longitude': -5.5673,
            'address': 'Médina de Meknès',
            'entry_price': 0.00,
            'opening_hours': 'Toute la journée',
            'best_time_to_visit': 'Soirée'
        },
        {
            'name': 'Mausolée Moulay Ismail',
            'description': 'Tombeau du sultan Moulay Ismail, fondateur de Meknès.',
            'category': 'mosquee',
            'latitude': 33.8928,
            'longitude': -5.5608,
            'address': 'Place Lalla Aouda, Meknès',
            'entry_price': 0.00,
            'opening_hours': '9h00 - 12h00, 15h00 - 18h00',
            'best_time_to_visit': 'Matin'
        },
    ],
    'Oujda': [
        {
            'name': 'Medina d\'Oujda',
            'description': 'Vieille ville historique avec souks traditionnels et architecture hispano-mauresque.',
            'category': 'monument',
            'latitude': 34.6810,
            'longitude': -1.9086,
            'address': 'Centre-ville, Oujda',
            'entry_price': 0.00,
            'opening_hours': 'Toute la journée',
            'best_time_to_visit': 'Matin'
        },
    ],
}

def create_sample_places():
    """Crée des lieux touristiques de test pour chaque ville"""
    created_count = 0
    
    for city_name, places_list in TOURISTIC_PLACES.items():
        try:
            city = City.objects.get(name=city_name)
            print(f"\n📌 Ajout des lieux pour {city_name}:")
            
            for place_data in places_list:
                # Vérifie si le lieu existe déjà
                if not Place.objects.filter(name=place_data['name'], city=city).exists():
                    place = Place.objects.create(
                        name=place_data['name'],
                        description=place_data['description'],
                        city=city,
                        category=place_data['category'],
                        latitude=place_data['latitude'],
                        longitude=place_data['longitude'],
                        address=place_data.get('address', ''),
                        entry_price=place_data.get('entry_price', 0),
                        opening_hours=place_data.get('opening_hours', ''),
                        best_time_to_visit=place_data.get('best_time_to_visit', ''),
                        is_featured=True  # Tous mis en avant pour le test
                    )
                    print(f"  ✅ {place.name}")
                    created_count += 1
                else:
                    print(f"  ⚠️ {place_data['name']} existe déjà")
        except City.DoesNotExist:
            print(f"  ❌ Ville '{city_name}' non trouvée dans la base")
    
    print(f"\n🎉 {created_count} lieux touristiques créés avec succès !")
    return created_count

if __name__ == '__main__':
    create_sample_places()
