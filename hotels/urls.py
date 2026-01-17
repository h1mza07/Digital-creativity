from django.urls import path
from . import views

urlpatterns = [
    path('city/<int:city_id>/', views.hotel_list_by_city, name='hotel_list_by_city'),
    path('<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
]