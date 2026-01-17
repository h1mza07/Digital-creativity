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


class TouristPlace(models.Model):
    PLACE_TYPES = [
        ('monument', _('Monument')),
        ('museum', _('Musée')),
        ('park', _('Parc')),
        ('beach', _('Plage')),
        ('market', _('Marché')),
        ('religious', _('Site religieux')),
        ('other', _('Autre')),
    ]
    
    name = models.CharField(_("Nom"), max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='tourist_places')
    description = models.TextField(_("Description"))
    type = models.CharField(_("Type"), max_length=20, choices=PLACE_TYPES)
    image = models.ImageField(_("Image"), upload_to='places/', null=True, blank=True)
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))
    address = models.CharField(_("Adresse"), max_length=300, blank=True)
    opening_hours = models.TextField(_("Horaires d'ouverture"), blank=True)
    price_range = models.CharField(_("Fourchette de prix"), max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Lieu touristique")
        verbose_name_plural = _("Lieux touristiques")
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.city.name}"