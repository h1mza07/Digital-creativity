from django.shortcuts import render
from django.http import HttpResponse

def worldcup_home(request):
    return HttpResponse("<h1>⚽ Coupe du Monde 2030</h1>")

def host_cities(request):
    return HttpResponse("<h1>🏟️ Villes hôtes</h1>")

def stadium_list(request):
    return HttpResponse("<h1>🏟️ Stades</h1>")