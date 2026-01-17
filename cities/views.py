from django.shortcuts import render
from django.http import HttpResponse
from .models import City  

def city_list(request):
    cities = City.objects.all()  
    return render(request, 'cities/city_list.html', {'cities': cities})  # REMPLACE CETTE LIGNE

def city_detail(request, slug):
    return HttpResponse(f"<h1>Détails ville : {slug}</h1>")