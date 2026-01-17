# places/urls.py
from django.urls import path
from . import views

app_name = 'places'  # Important pour les URLs namespaced

urlpatterns = [
    # Liste des lieux avec filtres optionnels
    path('', views.PlaceListView.as_view(), name='place_list'),
    
    # Carte interactive de tous les lieux
    path('map/', views.place_map_view, name='place_map'),
    
    # Détail d'un lieu par ID (version simple)
    path('<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    
    # Détail d'un lieu par ID et slug (version SEO-friendly)
    path('<int:pk>/<slug:slug>/', views.PlaceDetailView.as_view(), name='place_detail_slug'),
    
    # URL pour filtrer par ville (ex: /places/city/1/)
    path('city/<int:city_id>/', views.PlaceListView.as_view(), name='places_by_city'),
    
    # URL pour filtrer par catégorie (ex: /places/category/monument/)
    path('category/<str:category>/', views.PlaceListView.as_view(), name='places_by_category'),
    
    # URL de recherche (ex: /places/search/?q=marrakech)
    path('search/', views.PlaceListView.as_view(), name='place_search'),
]