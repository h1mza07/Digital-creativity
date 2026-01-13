from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler404
from django.shortcuts import render

def error_403(request, exception):
    return render(request, '403.html', status=403)

def error_404(request, exception):
    return render(request, '404.html', status=404)

handler403 = error_403
handler404 = error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
