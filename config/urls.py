from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('routes.urls')),  # Page d'accueil via routes
    path('cities/', include('cities.urls')),
    path('users/', include('users.urls')),
    path('', include('routes.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)