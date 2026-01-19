from django.shortcuts import render, get_object_or_404
from .models import Hotel

def hotel_list_by_city(request, city_id):
    hotels = Hotel.objects.filter(city_id=city_id)
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})
if query:
    hotels = hotels.filter(name__icontains=query)

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})