from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf.urls import handler403, handler404
from django.shortcuts import render

def error_403(request, exception):
    return render(request, '403.html', status=403)

def error_404(request, exception):
    return render(request, '404.html', status=404)

handler403 = error_403
handler404 = error_404

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('lieux/', include('places.urls')),
]

urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    
    path('cities/', include('cities.urls')),
    path('worldcup/', include('worldcup2030.urls')),
    path('users/', include('users.urls')),
    
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)