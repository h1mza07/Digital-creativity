from django.shortcuts import render, get_object_or_404
from .models import Hotel
from django.core.paginator import Paginator

def hotel_list(request):
    query = request.GET.get('q')
    hotels = Hotel.objects.all()

    if query:
        hotels = hotels.filter(name__icontains=query)

    paginator = Paginator(hotels, 5)  # 5 hôtels par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hotels/hotel_list.html', {
        'page_obj': page_obj,
        'query': query
    })

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})