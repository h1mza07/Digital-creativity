from django.db import models
from cities.models import City  # Importe le modèle City existant

class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du lieu")
    description = models.TextField(verbose_name="Description")
    city = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        related_name='places',
        verbose_name="Ville"
    )
    latitude = models.FloatField(verbose_name="Latitude", help_text="Ex: 31.6295")
    longitude = models.FloatField(verbose_name="Longitude", help_text="Ex: -7.9811")
    image = models.ImageField(
        upload_to='places/',
        blank=True,
        null=True,
        verbose_name="Image du lieu"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Lieu touristique"
        verbose_name_plural = "Lieux touristiques"

    def __str__(self):
        return f"{self.name} ({self.city.name})"
        # Dans places/models.py
latitude = models.FloatField(verbose_name="Latitude", blank=True, null=True)
longitude = models.FloatField(verbose_name="Longitude", blank=True, null=True)