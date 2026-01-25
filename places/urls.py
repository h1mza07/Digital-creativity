from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.places_list, name='places_list'),
    path('<int:id>/', views.place_detail, name='place_detail'),
    path('city/<int:city_id>/', views.city_places, name='city_places'),
]