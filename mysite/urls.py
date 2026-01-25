from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('hotels.urls')),
    path('routes/', include('routes.urls')),
     path('places/', include('places.urls')), 
     
]
