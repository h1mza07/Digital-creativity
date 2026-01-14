from django.db import migrations

def add_initial_cities(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    
    # Liste des villes marocaines avec coordonnées GPS
    cities_data = [
        {
            'name': 'Marrakech',
            'slug': 'marrakech',
            'description': 'Ville impériale connue pour sa médina, la place Jemaa el-Fna et ses palais.',
            'latitude': 31.6295,
            'longitude': -7.9811,
            'population': 928850
        },
        {
            'name': 'Casablanca',
            'slug': 'casablanca',
            'description': 'Plus grande ville du Maroc, centre économique avec la mosquée Hassan II.',
            'latitude': 33.5731,
            'longitude': -7.5898,
            'population': 3350000
        },
        {
            'name': 'Fès',
            'slug': 'fes',
            'description': 'Ville impériale abritant la plus ancienne médina du monde, Fès el-Bali.',
            'latitude': 34.0181,
            'longitude': -5.0078,
            'population': 1112072
        },
        {
            'name': 'Tanger',
            'slug': 'tanger',
            'description': 'Port stratégique sur le détroit de Gibraltar, mélange de cultures.',
            'latitude': 35.7595,
            'longitude': -5.8340,
            'population': 947952
        },
        {
            'name': 'Agadir',
            'slug': 'agadir',
            'description': 'Station balnéaire sur la côte atlantique, plages et climat ensoleillé.',
            'latitude': 30.4278,
            'longitude': -9.5981,
            'population': 600178
        },
        {
            'name': 'Rabat',
            'slug': 'rabat',
            'description': 'Capitale du Maroc, ville moderne avec des monuments historiques.',
            'latitude': 34.0209,
            'longitude': -6.8416,
            'population': 577827
        },
        {
            'name': 'Meknès',
            'slug': 'meknes',
            'description': 'Ville impériale connue pour ses portes monumentales et son mausolée.',
            'latitude': 33.8890,
            'longitude': -5.5556,
            'population': 632079
        },
        {
            'name': 'Oujda',
            'slug': 'oujda',
            'description': 'Ville de l\'est du Maroc, porte vers l\'Algérie.',
            'latitude': 34.6814,
            'longitude': -1.9086,
            'population': 551767
        }
    ]
    
    for city_data in cities_data:
        City.objects.get_or_create(
            name=city_data['name'],
            defaults={
                'slug': city_data['slug'],
                'description': city_data['description'],
                'latitude': city_data['latitude'],
                'longitude': city_data['longitude'],
                'population': city_data['population']
            }
        )
    
    print(f"✅ {len(cities_data)} villes ajoutées avec succès")

def remove_cities(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    City.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('cities', '0002_touristplace'),
    ]

    operations = [
        migrations.RunPython(add_initial_cities, remove_cities),
    ]