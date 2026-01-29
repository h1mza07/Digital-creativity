# places/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('<int:place_id>/', views.place_detail, name='place_detail'),
    path('map/', views.map_view, name='map_view'),
]