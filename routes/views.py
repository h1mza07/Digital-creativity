from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # AJOUTÉ : Import nécessaire pour le User de secours
from .models import Itinerary
#from .forms import ItineraryForm
from django.http import JsonResponse

def itinerary_list(request):
    """Affiche absolument TOUS les itinéraires sans filtrer par utilisateur pour le test"""
    itineraries = Itinerary.objects.all().order_by('-created_at')

    print(f"--- DEBUG: {itineraries.count()} itinéraires envoyés au template ---")

    return render(request, 'routes/itinerary_list.html', {
        'itineraries': itineraries
    })

@login_required
def itinerary_create(request):
    mapping_destinations = {
        'Sofitel': 'Stade Prince Moulay Abdellah, Rabat',
        'Premier Classe': 'Stade Prince Moulay Abdellah, Rabat',
        'Hostel Rabat': 'Stade Prince Moulay Abdellah, Rabat',
        'La Mamounia': 'Grand Stade de Marrakech',
        'Al Mansour': 'Grand Stade de Marrakech',
        'Backpackers Hostel': 'Grand Stade de Marrakech',
        'Four Seasons': 'Grand Stade de Casablanca, Benslimane',
        'Kenzi Business': 'Grand Stade de Casablanca, Benslimane',
        'Budget Hotel': 'Grand Stade de Casablanca, Benslimane',
        'Royal Atlas': 'Stade Adrar, Agadir',
        'Gadir Bay Hotel': 'Stade Adrar, Agadir',
        'Surf Hostel': 'Stade Adrar, Agadir',
        'Riad Fes': 'Complexe Sportif de Fès',
        'Fes Heritage': 'Complexe Sportif de Fès',
        'Fes Medina Hostel': 'Complexe Sportif de Fès',
    }

    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user
            
            hotel_selectionne = request.POST.get('hotel_name')
            itinerary.hotel_name = hotel_selectionne
            
            stade_destination = mapping_destinations.get(hotel_selectionne, "Stade de la Coupe du Monde, Maroc")
            itinerary.stadium_name = stade_destination 
            
            base_url = "https://www.google.com/maps/dir/?api=1" # URL de production plus fiable
            itinerary.google_maps_url = f"{base_url}&origin={hotel_selectionne}+Morocco&destination={stade_destination}&travelmode=driving"
            
            itinerary.save()
            return redirect('itinerary_list') # Redirige vers la liste après création
    else:
        form = ItineraryForm()
    
    return render(request, 'routes/itinerary_form.html', {'form': form, 'title': 'Créer un itinéraire'})

@login_required


def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'routes/itinerary_detail.html', {'itinerary': itinerary })

def get_google_maps_url(request):
    hotel = request.GET.get('hotel', '')
    stadium_name = request.GET.get('stadium', '')
    if hotel and stadium_name:
        map_url = f"https://www.google.com/maps/dir/?api=1&origin={hotel}&destination={stadium_name}&travelmode=driving"
        return JsonResponse({'success': True, 'map_url': map_url})
    return JsonResponse({'success': False, 'error': 'Paramètres manquants'}, status=400)