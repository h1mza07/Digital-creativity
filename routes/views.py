from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomItinerary, ItineraryStop, Itinerary
from places.models import Place
from hotels.models import Hotel

@login_required
def itinerary_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        itinerary = CustomItinerary.objects.create(user=request.user, title=title)
        return redirect('itinerary_detail', pk=itinerary.pk)
def itinerary_create(request):
    return render(request, 'routes/itinerary_form.html')

@login_required
def itinerary_detail(request, pk):
    itinerary = get_object_or_404(CustomItinerary, pk=pk, user=request.user)
    places = Place.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'routes/itinerary_detail.html', {
        'itinerary': itinerary,
        'places': places,
        'hotels': hotels
    })

@login_required
def add_stop(request, pk):
    itinerary = get_object_or_404(CustomItinerary, pk=pk, user=request.user)
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
    stop = get_object_or_404(ItineraryStop, id=stop_id, itinerary_id=itinerary_id)
    if stop.itinerary.user == request.user:
        stop.delete()
    return redirect('itinerary_detail', pk=itinerary_id)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
def itinerary_list(request):
    """
    Affiche la liste des itineraries publics
    """
    # Itineraries publics
    public_itineraries = Itinerary.objects.all()
    
    context = {
        'public_itineraries': public_itineraries,
        'title': 'Itinéraires'
    }
    
    # Itineraires personnels (si connecté)
    if request.user.is_authenticated:
        personal_itineraries = CustomItinerary.objects.filter(user=request.user)
        context['personal_itineraries'] = personal_itineraries
    
    return render(request, 'routes/itinerary_list.html', context)
=======
    # routes/views.py
from django.shortcuts import render

>>>>>>> Stashed changes
=======
    # routes/views.py
from django.shortcuts import render

>>>>>>> Stashed changes
