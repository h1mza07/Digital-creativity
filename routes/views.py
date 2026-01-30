from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # AJOUTÉ : Import nécessaire pour le User de secours
from .models import Itinerary
#from .forms import ItineraryForm
from django.http import JsonResponse

@login_required
def itinerary_list(request):
    itineraries = Itinerary.objects.all().order_by('-created_at') 
    print(f"DEBUG: {itineraries.count()} routes trouvées") 

    return render(request, 'routes/itinerary_list.html', {'itineraries': itineraries}) 
@login_required
def itinerary_create(request):
    # Mapping complet basé sur tes dossiers d'images (image_2dbd89.png)
    mapping_destinations = {
        # RABAT
        'Sofitel': ('Rabat', 'Stade Prince Moulay Abdellah'),
        'Premier': ('Rabat', 'Stade Prince Moulay Abdellah'),
        'Hostel': ('Rabat', 'Stade Prince Moulay Abdellah'),
        # MARRAKECH
        'Elmamounia': ('Marrakech', 'Grand Stade de Marrakech'),
        'Almansour': ('Marrakech', 'Grand Stade de Marrakech'),
        'Backparkershostelkech': ('Marrakech', 'Grand Stade de Marrakech'),
        # CASABLANCA
        'Fourseason': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        'Kenzibusiness': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        'Budget': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        # AGADIR
        'RoyalAtlas': ('Agadir', 'Stade Adrar'),
        'GadirBayHotel': ('Agadir', 'Stade Adrar'),
        'SurfHostel': ('Agadir', 'Stade Adrar'),
        # FES
        'Riadfes': ('Fès', 'Complexe Sportif de Fès'),
        'Fesheritage': ('Fès', 'Complexe Sportif de Fès'),
        'Fesmedinahostel': ('Fès', 'Complexe Sportif de Fès'),
    }

    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user
            
            hotel_selectionne = request.POST.get('hotel_name')
            
            # Récupération de la ville et du stade selon l'hôtel
            ville_stade = mapping_destinations.get(hotel_selectionne, ("Maroc", "Stade CM 2030"))
            itinerary.city = ville_stade[0]
            itinerary.stadium_name = ville_stade[1]
            
            # Génération de l'URL Google Maps automatique
            base_url = "https://www.google.com/maps/dir/?api=1"
            itinerary.google_maps_url = f"{base_url}&origin={hotel_selectionne}+{itinerary.city}+Morocco&destination={itinerary.stadium_name}&travelmode=driving"
            
            itinerary.save()
            return redirect('itinerary_list')
    else:
        form = ItineraryForm()
    
    return render(request, 'routes/itinerary_form.html', {'form': form})

@login_required


def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'routes/itinerary_detail.html', {'itinerary': itinerary })

def get_google_maps_url(request):
    hotel = request.GET.get('hotel', '')
    stadium = request.GET.get('stadium', '')
    if hotel and stadium:
        map_url = f"https://www.google.com/maps/dir/?api=1&origin={hotel}&destination={stadium}&travelmode=driving"
        return JsonResponse({'success': True, 'map_url': map_url})
    return JsonResponse({'success': False, 'error': 'Paramètres manquants'}, status=400)