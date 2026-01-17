from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import City

def home_page(request):
    return render(request, 'home.html')

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    return render(request, 'cities/city_detail.html', {'city': city})