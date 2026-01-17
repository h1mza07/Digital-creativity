from django.shortcuts import render
from django.http import HttpResponse

def city_list(request):
    return HttpResponse("<h1> Liste des villes marocaines</h1>")

def city_detail(request, slug):
    return HttpResponse(f"<h1>Détails ville : {slug}</h1>")