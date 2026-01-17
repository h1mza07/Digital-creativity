from django.urls import path
from . import views

urlpatterns = [
    path('', views.itinerary_list, name='itinerary_list'),
    path('search/', views.itinerary_search, name='itinerary_search'),
    path('profile/', views.profile_view, name='profile'),
]