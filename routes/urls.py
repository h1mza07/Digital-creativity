from django.urls import path
from . import views

urlpatterns = [
    path('my-itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itinerary/create/', views.itinerary_create, name='itinerary_create'),
    path('itinerary/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
    path('itinerary/<int:pk>/add-stop/', views.add_stop, name='add_stop'),
    path('itinerary/<int:itinerary_id>/remove-stop/<int:stop_id>/', views.remove_stop, name='remove_stop'),
]