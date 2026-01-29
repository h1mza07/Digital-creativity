# hotels/migrations/0004_add_hotels_data.py

from django.db import migrations
from django.core.files import File
import os

def add_hotels(apps, schema_editor):
    Hotel = apps.get_model('hotels', 'Hotel')
    City = apps.get_model('cities', 'City')
    
    # Récupérer les villes existantes
    cities_map = {city.name: city for city in City.objects.all()}
    
    # Vérifier les villes nécessaires
    required_cities = ['Marrakech', 'Rabat', 'Casablanca', 'Fès', 'Agadir']
    for city_name in required_cities:
        if city_name not in cities_map:
            raise ValueError(f"Ville '{city_name}' introuvable. Appliquez d'abord: python manage.py migrate cities")
    
    hotels_data = [
        # ========== MARRAKECH ==========
        {
            'name': 'Al Mansour Hotel',
            'description': 'Hôtel 5 étoiles de luxe au cœur de la médina de Marrakech',
            'city': cities_map['Marrakech'],
            'rating': 5,
            'price': 220.00,
            'image_filename': 'marrakech/almansour.jpg'
        },
        {
            'name': 'El Mamounia Hotel',
            'description': 'Hôtel 4 étoiles moderne à proximité de la place Jemaa el-Fna',
            'city': cities_map['Marrakech'],
            'rating': 4,
            'price': 130.00,
            'image_filename': 'marrakech/elmamounia.jpg'
        },
        {
            'name': 'Marrakech Backpackers Hostel',
            'description': 'Hostel économique pour voyageurs avec cuisine commune',
            'city': cities_map['Marrakech'],
            'rating': 3,
            'price': 35.00,
            'image_filename': 'marrakech/backbarkershostelkech.jpg'
        },
        
        # ========== RABAT ==========
        {
            'name': 'Sofitel Rabat',
            'description': 'Hôtel 5 étoiles avec vue sur l\'Atlantique',
            'city': cities_map['Rabat'],
            'rating': 5,
            'price': 240.00,
            'image_filename': 'rabat/sofitel.jpg'
        },
        {
            'name': 'Rabat Premier Hotel',
            'description': 'Hôtel 4 étoiles moderne dans le centre-ville',
            'city': cities_map['Rabat'],
            'rating': 4,
            'price': 120.00,
            'image_filename': 'rabat/premier.jpg'
        },
        {
            'name': 'Rabat Travelers Hostel',
            'description': 'Hostel abordable près de la Kasbah des Oudayas',
            'city': cities_map['Rabat'],
            'rating': 3,
            'price': 30.00,
            'image_filename': 'rabat/hostel.jpg'
        },
        
        # ========== CASABLANCA ==========
        {
            'name': 'Four Seasons Casablanca',
            'description': 'Hôtel 5 étoiles de luxe face à l\'océan Atlantique',
            'city': cities_map['Casablanca'],
            'rating': 5,
            'price': 450.00,
            'image_filename': 'casablanca/Fourseason.jpg'
        },
        {
            'name': 'Kenzi Business Hotel',
            'description': 'Hôtel 4 étoiles idéal pour voyageurs d\'affaires',
            'city': cities_map['Casablanca'],
            'rating': 4,
            'price': 150.00,
            'image_filename': 'casablanca/kenzibusiness.jpg'
        },
        {
            'name': 'Casablanca Budget Hostel',
            'description': 'Hostel économique pour backpackers au centre-ville',
            'city': cities_map['Casablanca'],
            'rating': 3,
            'price': 40.00,
            'image_filename': 'casablanca/budget.jpg'
        },
        
        # ========== FÈS ==========
        {
            'name': 'Riad Fès',
            'description': 'Riad 5 étoiles de prestige dans la médina de Fès',
            'city': cities_map['Fès'],
            'rating': 5,
            'price': 210.00,
            'image_filename': 'fes/Riadfes.jpg'
        },
        {
            'name': 'Fès Heritage Hotel',
            'description': 'Hôtel 4 étoiles avec architecture traditionnelle',
            'city': cities_map['Fès'],
            'rating': 4,
            'price': 110.00,
            'image_filename': 'fes/fesheritage.jpg'
        },
        {
            'name': 'Fès Medina Hostel',
            'description': 'Hostel authentique au cœur de la médina',
            'city': cities_map['Fès'],
            'rating': 3,
            'price': 28.00,
            'image_filename': 'fes/fesmedinahostel.jpg'
        },
        
        # ========== AGADIR ==========
        {
            'name': 'Royal Atlas Agadir',
            'description': 'Hôtel 5 étoiles sur la plage avec vue sur l\'océan',
            'city': cities_map['Agadir'],
            'rating': 5,
            'price': 230.00,
            'image_filename': 'agadir/RoyalAtlas.jpg'
        },
        {
            'name': 'Gadir Bay Hotel',
            'description': 'Hôtel 4 étoiles moderne avec accès direct à la plage',
            'city': cities_map['Agadir'],
            'rating': 4,
            'price': 140.00,
            'image_filename': 'agadir/gadirBayHotel.jpg'
        },
        {
            'name': 'Surf Hostel Agadir',
            'description': 'Hostel pour surfeurs et voyageurs avec ambiance décontractée',
            'city': cities_map['Agadir'],
            'rating': 3,
            'price': 32.00,
            'image_filename': 'agadir/SurfHostel.jpg'
        },
    ]
    
    for hotel_data in hotels_data:
        image_filename = hotel_data.pop('image_filename')
        hotel = Hotel.objects.create(**hotel_data)
        
        image_path = os.path.join('hotels', 'static', 'hotels', 'images', image_filename)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                hotel.image.save(os.path.basename(image_path), File(img_file), save=True)

def remove_hotels(apps, schema_editor):
    Hotel = apps.get_model('hotels', 'Hotel')
    hotels_to_delete = [
        'Al Mansour Hotel', 'El Mamounia Hotel', 'Marrakech Backpackers Hostel',
        'Sofitel Rabat', 'Rabat Premier Hotel', 'Rabat Travelers Hostel',
        'Four Seasons Casablanca', 'Kenzi Business Hotel', 'Casablanca Budget Hostel',
        'Riad Fès', 'Fès Heritage Hotel', 'Fès Medina Hostel',
        'Royal Atlas Agadir', 'Gadir Bay Hotel', 'Surf Hostel Agadir'
    ]
    Hotel.objects.filter(name__in=hotels_to_delete).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_image'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_hotels, remove_hotels),
    ]