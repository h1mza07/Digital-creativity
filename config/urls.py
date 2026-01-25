from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('worldcup2030/', include('worldcup2030.urls')),
    path('routes/', include('routes.urls')),
    path('cities/', include('cities.urls')),
    path('test-villes/', TemplateView.as_view(template_name='cities/list.html'), name='test_villes'),
    path('users/', include('users.urls')),
    path('places/', include('places.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)