
from django.urls import path
from . import views 

#blabla
urlpatterns = [
    # Liste des itinéraires
    path('', views.itinerary_list, name='itinerary_list'),  
    
    # Recherche d'itinéraires
    path('search/', views.itinerary_search, name='itinerary_search'),
    
    # Page "À propos"
    path('about/', views.about, name='about'),
    
    # Vue temporaire pour le profil (à améliorer plus tard)
    path('profile/', views.profile_view, name='profile'),

    path('', views.home, name='home'),
]