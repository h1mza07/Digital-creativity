from django.urls import path
from . import views

urlpatterns = [
    path('city/<int:city_id>/', views.hotel_list_by_city, name='hotel_list_by_city'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('', views.hotel_list, name='hotel_list'),
]