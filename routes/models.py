from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from places.models import Place
from hotels.models import Hotel
from cities.models import City

class Itinerary(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Facile'),
        ('medium', 'Moyen'),
        ('hard', 'Difficile'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hotel_name = models.CharField(max_length=200, verbose_name="Hôtel de départ")
    stadium_name = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    
    description = models.TextField(blank=True)
    duration_days = models.PositiveIntegerField(default=1, help_text="Durée en jours")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    google_maps_url = models.URLField(max_length=500, null=True, blank=True)
    
    cities = models.ManyToManyField(City, related_name='itineraries_list', blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel_name} vers {self.stadium_name}"

# --- AJOUTÉ : Le modèle CustomItinerary qui manquait ---
class CustomItinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"

class ItineraryStop(models.Model):
    STOP_TYPES = [
        ('place', 'Lieu touristique'),
        ('hotel', 'Hôtel'),
        ('city', 'Ville'),
        ('other', 'Autre'),
    ]
    
    custom_itinerary = models.ForeignKey('CustomItinerary', related_name='stops', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    stop_type = models.CharField(max_length=10, choices=STOP_TYPES, default='place')
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    custom_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Nom personnalisé")
    description = models.TextField(blank=True, null=True)
    day_number = models.PositiveIntegerField(default=1, help_text="Jour de l'itinéraire")
    duration_hours = models.FloatField(default=2.0, help_text="Durée estimée en heures")

    class Meta:
        ordering = ['custom_itinerary', 'day_number', 'order']
        verbose_name = "Étape d'itinéraire"
        verbose_name_plural = "Étapes d'itinéraire"

    def __str__(self):
        return f"Étape {self.order} - {self.custom_name or 'Sans nom'}"

class ItineraryLike(models.Model):
    
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['itinerary', 'user']
    
    def __str__(self):
        # Corrigé : utilise hotel_name au lieu de name
        return f"{self.user.username} aime l'itinéraire {self.itinerary.hotel_name}"
