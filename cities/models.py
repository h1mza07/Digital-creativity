from django.db import models
from django.utils.translation import gettext_lazy as _

class City(models.Model):
    name = models.CharField(_("Nom"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to='cities/', null=True, blank=True)
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))
    population = models.IntegerField(_("Population"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Ville")
        verbose_name_plural = _("Villes")
        ordering = ['name']
    
    def __str__(self):
        return self.name