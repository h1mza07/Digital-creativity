from django.shortcuts import render, get_object_or_404
from .models import Itinerary

def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'routes/itinerary_list.html', {'itineraries': itineraries})

def itinerary_detail(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    return render(request, 'routes/itinerary_detail.html', {'itinerary': itinerary})