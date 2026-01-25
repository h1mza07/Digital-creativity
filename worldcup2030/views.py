from django.shortcuts import render

def worldcup_home(request):
    """
    Page d'accueil principale de la Coupe du Monde 2030
    Utilise le template: worldcup2030/index.html
    """
    # Données dynamiques pour le template
    context = {
        'page_title': 'Coupe du Monde 2030 - Maroc Tourisme',
        
        # Villes hôtes
        'host_cities': [
            {
                'name': 'Casablanca',
                'stadium': 'Grand Stade de Casablanca',
                'capacity': '93,000 places',
                'status': 'En construction',
                'status_class': 'bg-success'
            },
            {
                'name': 'Rabat',
                'stadium': 'Stade Moulay Abdellah',
                'capacity': '68,000 places',
                'status': 'Rénovation',
                'status_class': 'bg-warning text-dark'
            },
            {
                'name': 'Marrakech',
                'stadium': 'Stade de Marrakech',
                'capacity': '45,000 places',
                'status': 'Opérationnel',
                'status_class': 'bg-success'
            },
            {
                'name': 'Tanger',
                'stadium': 'Stade Ibn Batouta',
                'capacity': '65,000 places',
                'status': 'Extension',
                'status_class': 'bg-info'
            },
            {
                'name': 'Agadir',
                'stadium': 'Stade Adrar',
                'capacity': '45,000 places',
                'status': 'Opérationnel',
                'status_class': 'bg-success'
            },
        ],
        
        # Impact touristique
        'tourist_impacts': [
            {'icon': '🚀', 'title': 'Augmentation du tourisme', 'desc': 'Prévision : +40% de visiteurs'},
            {'icon': '🏨', 'title': 'Capacité hôtelière', 'desc': '50,000 chambres supplémentaires'},
            {'icon': '🚇', 'title': 'Infrastructures', 'desc': 'Nouvelles lignes de tramway'},
            {'icon': '💼', 'title': 'Emplois', 'desc': '100,000 emplois créés'},
            {'icon': '🌍', 'title': 'Image internationale', 'desc': 'Destination touristique premium'},
        ],
        
        # Dates importantes
        'important_dates': [
            {'icon': '✅', 'text': '2030 : Année de la compétition'},
            {'icon': '📍', 'text': '3 pays : Maroc, Espagne, Portugal'},
            {'icon': '🏟️', 'text': '10 stades prévus au Maroc'},
            {'icon': '👥', 'text': '48 équipes participantes'},
        ],
        
        # Statistiques
        'stats': [
            {'value': '3', 'label': 'Pays organisateurs'},
            {'value': '10', 'label': 'Stades au Maroc'},
            {'value': '48', 'label': 'Équipes'},
            {'value': '104', 'label': 'Matchs totaux'},
        ]
    }
    
    return render(request, 'worldcup2030/index.html', context)


def host_cities(request):
    """
    Page détaillée des villes hôtes
    """
    context = {
        'page_title': 'Villes Hôtes - CM 2030',
        'cities': [
            {'name': 'Casablanca', 'country': 'Maroc', 'population': '3.7M', 'stadium': 'Grand Stade de Casablanca'},
            {'name': 'Rabat', 'country': 'Maroc', 'population': '1.8M', 'stadium': 'Stade Moulay Abdellah'},
            {'name': 'Marrakech', 'country': 'Maroc', 'population': '1.0M', 'stadium': 'Stade de Marrakech'},
            {'name': 'Madrid', 'country': 'Espagne', 'population': '3.3M', 'stadium': 'Santiago Bernabéu'},
            {'name': 'Barcelone', 'country': 'Espagne', 'population': '1.6M', 'stadium': 'Camp Nou'},
            {'name': 'Lisbonne', 'country': 'Portugal', 'population': '2.9M', 'stadium': 'Estádio da Luz'},
        ]
    }
    return render(request, 'worldcup2030/host_cities.html', context)


def stadium_list(request):
    """
    Page des stades
    """
    context = {
        'page_title': 'Stades - CM 2030',
        'stadiums': [
            {'name': 'Grand Stade de Casablanca', 'city': 'Casablanca', 'capacity': 93000, 'country': '🇲🇦 Maroc'},
            {'name': 'Stade Moulay Abdellah', 'city': 'Rabat', 'capacity': 68000, 'country': '🇲🇦 Maroc'},
            {'name': 'Stade de Marrakech', 'city': 'Marrakech', 'capacity': 45000, 'country': '🇲🇦 Maroc'},
            {'name': 'Santiago Bernabéu', 'city': 'Madrid', 'capacity': 81000, 'country': '🇪🇸 Espagne'},
            {'name': 'Camp Nou', 'city': 'Barcelone', 'capacity': 99000, 'country': '🇪🇸 Espagne'},
            {'name': 'Estádio da Luz', 'city': 'Lisbonne', 'capacity': 65000, 'country': '🇵🇹 Portugal'},
        ]
    }
    return render(request, 'worldcup2030/stadiums.html', context)