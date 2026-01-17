
from django.urls import path
from . import views

urlpatterns = [
    # Liste des itinéraires
    path('', views.itinerary_list, name='itinerary_list'),  # 👈 /routes/ affiche la liste
    
    # Recherche d'itinéraires
    path('search/', views.itinerary_search, name='itinerary_search'),
    
    # Page "À propos"
    path('about/', views.about, name='about'),
    
    # Vue temporaire pour le profil (à améliorer plus tard)
    path('profile/', views.profile_view, name='profile'),
    
    # Détail d'un itinéraire
    path('itinerary/<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),
]