# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from users.views import profile 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routes/', include('routes.urls')),
    path('profile/', profile, name='profile'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)