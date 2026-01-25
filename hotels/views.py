from django.shortcuts import render, get_object_or_404
from .models import Hotel
from django.core.paginator import Paginator

def hotel_list(request):
    query = request.GET.get('q')
    if query:
        hotels = Hotel.objects.filter(
            name__icontains=query
        ) | Hotel.objects.filter(
            city__name__icontains=query
        )
    else:
        hotels = Hotel.objects.all()
    
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})

def hotel_list_by_city(request, city_id):
    return render(request, 'hotels/hotel_list.html', {
        'title': f'Hôtels - Ville ID {city_id}'
    })