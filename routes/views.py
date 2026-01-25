from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomItinerary, ItineraryStop, Itinerary
from places.models import Place
from hotels.models import Hotel

@login_required
def itinerary_list(request):
    public_itineraries = Itinerary.objects.filter(user__isnull=True)  # Itinéraires publics
    
    if request.user.is_authenticated:
        personal_itineraries = Itinerary.objects.filter(user=request.user)  # Itinéraires personnels
    else:
        personal_itineraries = []
    
    return render(request, 'routes/itinerary_list.html', {
        'public_itineraries': public_itineraries,
        'personal_itineraries': personal_itineraries,
        'title': 'Mes itinéraires'
    })
    
    # Itineraires personnels (si connecté)
    if request.user.is_authenticated:
        personal_itineraries = Itinerary.objects.filter(user=request.user)
        context['personal_itineraries'] = personal_itineraries
    
    return render(request, 'routes/itinerary_list.html', context)

@login_required
def itinerary_create(request):
    """
    Crée un nouvel itinéraire personnalisé
    """
    if request.method == "POST":
        title = request.POST.get('title')
        itinerary = Itinerary.objects.create(
            user=request.user, 
            title=title, 
            name=name, 
            description=description,)
        return redirect('itinerary_detail', pk=itinerary.pk)


def itinerary_detail(request, pk):
    """
    Affiche le détail d'un itinéraire personnalisé
    """
    itinerary = get_object_or_404(Itinerary, pk=pk, user=request.user)
    places = Place.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'routes/itinerary_detail.html', {
        'itinerary': itinerary,
        'places': places,
        'hotels': hotels
    })

@login_required
def add_stop(request, pk):
    """
    Ajoute une étape (lieu ou hôtel) à un itinéraire
    """
    itinerary = get_object_or_404(Itinerary, pk=pk, user=request.user)
    if request.method == "POST":
        place_id = request.POST.get('place')
        hotel_id = request.POST.get('hotel')
        order = itinerary.stops.count() + 1

        if place_id:
            place = get_object_or_404(Place, id=place_id)
            ItineraryStop.objects.create(itinerary=itinerary, order=order, place=place)
        elif hotel_id:
            hotel = get_object_or_404(Hotel, id=hotel_id)
            ItineraryStop.objects.create(itinerary=itinerary, order=order, hotel=hotel)

    return redirect('itinerary_detail', pk=pk)

@login_required
def remove_stop(request, itinerary_id, stop_id):
    """
    Supprime une étape d'un itinéraire
    """
    stop = get_object_or_404(ItineraryStop, id=stop_id, itinerary_id=itinerary_id)
    if stop.itinerary.user == request.user:
        stop.delete()
    return redirect('itinerary_detail', pk=itinerary_id)
    public_itineraries = Itinerary.objects.all()
    return render(request, 'routes/itinerary_list.html', {
        'public_itineraries': public_itineraries,
        'title': 'Liste des itinéraires'
    })

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'routes/itinerary_detail.html', {
        'itinerary': itinerary
    })

def itinerary_create(request):
    # on redirige vers la liste
    from django.shortcuts import redirect
    return redirect('itinerary_list')

