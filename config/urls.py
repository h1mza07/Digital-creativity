from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from places import views 
from hotels import views as hotels_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('worldcup2030/', include('worldcup2030.urls')),
    path('routes/', include('routes.urls')),
    path('cities/', include('cities.urls')),
    path('users/', include('users.urls')),
    path('places/', include('places.urls')),
    path('places/map/', views.map_view, name='map_view'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
    path('hotels/', hotels_views.hotel_list, name='hotel_list'),
    path('hotels/<int:pk>/', hotels_views.hotel_detail, name='hotel_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)