from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Itinerary

@login_required
def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'routes/itinerary_list.html', {
        'itineraries': itineraries,
        'title': 'Itinéraires Hôtel → Stade'
    })

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'routes/itinerary_detail.html', {
        'itinerary': itinerary
    })