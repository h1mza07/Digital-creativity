from django.apps import AppConfig
import os

class RoutesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'routes'
    path = os.path.dirname(__file__)