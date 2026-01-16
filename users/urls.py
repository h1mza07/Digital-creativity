from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('favorite/add/<str:place_name>/', views.add_favorite, name='add_favorite'),
    path('favorite/remove/<int:fav_id>/', views.remove_favorite, name='remove_favorite'),
]
