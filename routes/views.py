from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Itinerary
from django.http import JsonResponse

@login_required
def itinerary_list(request):
    itineraries = Itinerary.objects.all().order_by('-created_at') 
    print(f"DEBUG: {itineraries.count()} routes trouvées") 
    return render(request, 'routes/itinerary_list.html', {'itineraries': itineraries})

@login_required
def itinerary_create(request):
    mapping_destinations = {
        'Sofitel': ('Rabat', 'Stade Prince Moulay Abdellah'),
        'Premier': ('Rabat', 'Stade Prince Moulay Abdellah'),
        'Hostel': ('Rabat', 'Stade Prince Moulay Abdellah'),
        'Elmamounia': ('Marrakech', 'Grand Stade de Marrakech'),
        'Almansour': ('Marrakech', 'Grand Stade de Marrakech'),
        'Backparkershostelkech': ('Marrakech', 'Grand Stade de Marrakech'),
        'Fourseason': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        'Kenzibusiness': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        'Budget': ('Casablanca', 'Grand Stade de Casablanca (Benslimane)'),
        'RoyalAtlas': ('Agadir', 'Stade Adrar'),
        'GadirBayHotel': ('Agadir', 'Stade Adrar'),
        'SurfHostel': ('Agadir', 'Stade Adrar'),
        'Riadfes': ('Fès', 'Complexe Sportif de Fès'),
        'Fesheritage': ('Fès', 'Complexe Sportif de Fès'),
        'Fesmedinahostel': ('Fès', 'Complexe Sportif de Fès'),
    }
    
    if request.method == 'POST':
        hotel_selectionne = request.POST.get('hotel_name')
        
        if hotel_selectionne:
            ville_stade = mapping_destinations.get(hotel_selectionne, ("Maroc", "Stade CM 2030"))
            
            itinerary = Itinerary.objects.create(
                user=request.user,
                hotel_name=hotel_selectionne,
                city=ville_stade[0],
                stadium_name=ville_stade[1],
                google_maps_url=f"https://www.google.com/maps/dir/?api=1&origin={hotel_selectionne}+{ville_stade[0]}+Morocco&destination={ville_stade[1]}&travelmode=driving"
            )
            return redirect('itinerary_list')
    
    return render(request, 'routes/itinerary_form.html')

@login_required
def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'routes/itinerary_detail.html', {'itinerary': itinerary})

def get_google_maps_url(request):
    hotel = request.GET.get('hotel', '')
    stadium = request.GET.get('stadium', '')
    if hotel and stadium:
        map_url = f"https://www.google.com/maps/dir/?api=1&origin={hotel}&destination={stadium}&travelmode=driving"
        return JsonResponse({'success': True, 'map_url': map_url})
    return JsonResponse({'success': False, 'error': 'Paramètres manquants'}, status=400)