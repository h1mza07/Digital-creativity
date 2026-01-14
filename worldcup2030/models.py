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
    class Stadium(models.Model):
    name = models.CharField(_("Nom du stade"), max_length=200)
    host_city = models.ForeignKey(HostCity, on_delete=models.CASCADE, related_name='stadiums')
    capacity = models.IntegerField(_("Capacité"))
    construction_year = models.IntegerField(_("Année de construction"))
    image = models.ImageField(_("Image"), upload_to='stadiums/', null=True, blank=True)
    description = models.TextField(_("Description"), blank=True)
    address = models.CharField(_("Adresse"), max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Stade")
        verbose_name_plural = _("Stades")
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.host_city.city.name}"