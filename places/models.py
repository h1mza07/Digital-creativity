from django.db import models
from cities.models import City

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='stadiums')
    address = models.CharField(max_length=300, blank=True)
    capacity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='stadiums/', blank=True, null=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    built_year = models.IntegerField(null=True, blank=True)
    is_world_cup_venue = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.city.name})"
    
    class Meta:
        ordering = ['name']
        verbose_name = "Stade"
        verbose_name_plural = "Stades"


class Place(models.Model):
    PLACE_TYPE_CHOICES = [
        ('monument', 'Monument'),
        ('museum', 'Musée'),
        ('park', 'Parc'),
        ('market', 'Marché'),
        ('restaurant', 'Restaurant'),
        ('other', 'Autre'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    place_type = models.CharField(max_length=50, choices=PLACE_TYPE_CHOICES, default='other')
    address = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    entrance_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_free = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.city.name})"
    
    class Meta:
        ordering = ['name']
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"