# routes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Itinerary

@login_required
def itinerary_list(request):
    """
    Affiche UNIQUEMENT les itinéraires hôtel → stade de l'utilisateur connecté
    """
    # 🔑 FILTRAGE : ne montre que les itinéraires avec hôtel + stade
    itineraries = Itinerary.objects.filter(
        created_by=request.user,
        hotel__isnull=False,
        stadium__isnull=False
    ).select_related('hotel', 'stadium', 'created_by').order_by('-created_at')
    
    context = {
        'itineraries': itineraries,
        'title': 'Itinéraires Hôtel → Stade',
        'has_itineraries': itineraries.exists()
    }
    
    return render(request, 'routes/itinerary_list.html', context)


@login_required
def itinerary_detail(request, pk):
    """
    Affiche les détails d'un itinéraire spécifique
    """
    # 🔑 Vérifie que l'itinéraire appartient à l'utilisateur
    itinerary = get_object_or_404(
        Itinerary, 
        pk=pk, 
        created_by=request.user
    )
    
    context = {
        'itinerary': itinerary,
        'title': itinerary.title
    }
    
    return render(request, 'routes/itinerary_detail.html', context)


@login_required
def itinerary_create(request):
    """
    Crée un nouvel itinéraire hôtel → stade
    """
    from hotels.models import Hotel
    from places.models import Stadium
    
    if request.method == 'POST':
        # Récupérer les données du formulaire
        hotel_id = request.POST.get('hotel')
        stadium_id = request.POST.get('stadium')
        title = request.POST.get('title')
        description = request.POST.get('description')
        difficulty = request.POST.get('difficulty', 'facile')
        best_season = request.POST.get('best_season', '')
        required_equipment = request.POST.get('required_equipment', '')
        contact_info = request.POST.get('contact_info', '')
        
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            stadium = Stadium.objects.get(id=stadium_id)
            
            # Créer l'itinéraire
            itinerary = Itinerary.objects.create(
                title=title,
                description=description,
                hotel=hotel,
                stadium=stadium,
                city=hotel.city.name if hotel.city else 'Marrakech',
                difficulty=difficulty,
                best_season=best_season,
                required_equipment=required_equipment,
                contact_info=contact_info,
                hotel_name=hotel.name,
                hotel_rating=hotel.rating,
                hotel_price=hotel.price,
                hotel_address=hotel.address,
                stadium_name=stadium.name,
                stadium_address=stadium.address,
                distance=10.5,  # Valeur par défaut, à calculer avec API
                total_price=hotel.price,
                created_by=request.user
            )
            
            messages.success(request, 'Itinéraire créé avec succès !')
            return redirect('routes:itinerary_detail', pk=itinerary.pk)
            
        except Exception as e:
            messages.error(request, f'Erreur lors de la création : {str(e)}')
    
    # GET request - afficher le formulaire
    hotels = Hotel.objects.all().select_related('city')
    stadiums = Stadium.objects.all().select_related('city')
    
    context = {
        'hotels': hotels,
        'stadiums': stadiums,
        'title': 'Créer un itinéraire'
    }
    
    return render(request, 'routes/itinerary_form.html', context)


@login_required
def itinerary_delete(request, pk):
    """
    Supprime un itinéraire
    """
    itinerary = get_object_or_404(Itinerary, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        itinerary.delete()
        messages.success(request, 'Itinéraire supprimé avec succès !')
        return redirect('routes:itinerary_list')
    
    context = {
        'itinerary': itinerary,
        'title': 'Supprimer l\'itinéraire'
    }
    
    return render(request, 'routes/itinerary_confirm_delete.html', context)