# config/views.py
from django.shortcuts import render

def home(request):
    """Page d'accueil du projet"""
    return render(request, 'home.html')