
# routes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itineraries/', views.itinerary_list, name='itinerary_list'),  # ✅
    path('about/', views.about, name='about'),
    path('search/', views.itinerary_search, name='itinerary_search'),
    path('profile/', views.profile_view, name='profile'),
]