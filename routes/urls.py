from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Liste des itinéraires
    path('itineraries/', views.itinerary_list, name='itinerary_list'),

    # Page "À propos"
    path('about/', views.about, name='about'),

    # Recherche d'itinéraires
    path('search/', views.itinerary_search, name='itinerary_search'),

    # Vue temporaire pour le profil
    path('profile/', views.profile_view, name='profile'),

    # Détail d'un itinéraire
    path('itinerary/<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),

    # Ajout d'un commentaire sur un itinéraire
    path('itinerary/<int:itinerary_id>/comment/', views.add_comment, name='add_comment'),
]