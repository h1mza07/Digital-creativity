from django.urls import path
from . import views

urlpatterns = [
    path('', views.itinerary_list, name='itinerary_list'),
    path('<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),
]