from django.urls import path
from . import views

urlpatterns = [
    path('', views.worldcup_home, name='home'),
    path('host-cities/', views.host_cities, name='host_cities'),
    path('stadiums/', views.stadium_list, name='stadium_list'),
]