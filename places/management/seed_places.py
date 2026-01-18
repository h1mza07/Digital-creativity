# places/management/commands/seed_places.py
from django.core.management.base import BaseCommand
from places.models import Place, City

class Command(BaseCommand):
    help = 'Ajoute des données de test pour les lieux touristiques'
    
    def handle(self, *args, **kwargs):
        # Assure-toi d'avoir des villes créées
        cities = {
            'marrakech': City.objects.get_or_create(name='Marrakech')[0],
            'casablanca': City.objects.get_or_create(name='Casablanca')[0],
            'fes': City.objects.get_or_create(name='Fès')[0],
        }
        
        places_data = [
            {
                'name': 'Jardin Majorelle',
                'description': 'Jardin botanique créé par le peintre Jacques Majorelle.',
                'city': cities['marrakech'],
                'category': Place.CATEGORY_GARDEN,
                'latitude': 31.6412,
                'longitude': -8.0014,
            },
            {
                'name': 'Hassan II Mosque',
                'description': 'Plus grande mosquée du Maroc avec un minaret de 210 mètres.',
                'city': cities['casablanca'],
                'category': Place.CATEGORY_RELIGIOUS,
                'latitude': 33.6085,
                'longitude': -7.6326,
            },
            {
                'name': 'Medina de Fès',
                'description': 'Vieille ville médiévale classée au patrimoine mondial de l\'UNESCO.',
                'city': cities['fes'],
                'category': Place.CATEGORY_MONUMENT,
                'latitude': 34.0626,
                'longitude': -4.9730,
            },
        ]
        
        for data in places_data:
            Place.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
        
        self.stdout.write(self.style.SUCCESS('Données de test ajoutées avec succès !'))