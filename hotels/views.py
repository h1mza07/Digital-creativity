from django.shortcuts import render, get_object_or_404
from .models import Hotel
from django.core.paginator import Paginator

def hotel_list(request):
    query = request.GET.get('q')
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})

def hotel_list_by_city(request, city_id):
    return render(request, 'hotels/hotel_list.html', {
        'title': f'Hôtels - Ville ID {city_id}'
    })