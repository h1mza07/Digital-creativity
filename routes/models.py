from django.db import models
from cities.models import City

class Itinerary(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Facile'),
        ('medium', 'Moyen'),
        ('hard', 'Difficile'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_days = models.PositiveIntegerField(help_text="Durée en jours")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    cities = models.ManyToManyField(City, related_name='itineraries')
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.duration_days} jours)".
