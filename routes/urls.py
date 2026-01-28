from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('itinerary_list'), name='routes_root'),
    path('my-itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itinerary/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
]