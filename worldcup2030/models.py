from django.db import models
from django.utils.translation import gettext_lazy as _
from cities.models import City

class HostCity(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, related_name='worldcup_host')
    is_host = models.BooleanField(_("Ville hôte"), default=True)
    stadium_capacity = models.IntegerField(_("Capacité du stade"))
    matches_count = models.IntegerField(_("Nombre de matchs"))
    infrastructure_details = models.TextField(_("Infrastructures"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Ville hôte")
        verbose_name_plural = _("Villes hôtes")
        ordering = ['city__name']
    
    def __str__(self):
        return f"{self.city.name} (Ville hôte CM 2030)"