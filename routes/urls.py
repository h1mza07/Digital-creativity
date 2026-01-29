# routes/urls.py
from django.urls import path
from . import views

app_name = 'routes'

urlpatterns = [
    # Liste des itinéraires
    path('my-itineraries/', views.itinerary_list, name='itinerary_list'),
    
    # Détails d'un itinéraire
    path('my-itineraries/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
    
    # Créer un itinéraire
    path('my-itineraries/create/', views.itinerary_create, name='itinerary_create'),
    
    # Supprimer un itinéraire
    path('my-itineraries/<int:pk>/delete/', views.itinerary_delete, name='itinerary_delete'),
]