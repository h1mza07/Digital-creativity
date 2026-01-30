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
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_days = models.PositiveIntegerField(help_text="Durée en jours")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    cities = models.ManyToManyField(City, related_name='itineraries')
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)
    
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=3,
        help_text="Note sur 5 étoiles"  
    )
    views_count = models.IntegerField(default=0, verbose_name="Nombre de vues")
    
    # Ajout des champs de date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Nouveau champ pour indiquer si l'itinéraire est public
    is_public = models.BooleanField(default=True, verbose_name="Public")
    
    def __str__(self):
        return f"{self.name} ({self.duration_days} jours)"


class Comment(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, default="Anonyme")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commentaire par {self.author} sur {self.itinerary.name}"


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
    
    custom_itinerary = models.ForeignKey(CustomItinerary, related_name='stops', on_delete=models.CASCADE)
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
        if self.place:
            return f"Jour {self.day_number} - {self.place.name}"
        elif self.hotel:
            return f"Jour {self.day_number} - {self.hotel.name} (Hôtel)"
        elif self.city:
            return f"Jour {self.day_number} - {self.city.name}"
        else:
            return f"Jour {self.day_number} - {self.custom_name or 'Étape personnalisée'}"

    @property
    def name(self):
        """Retourne le nom approprié selon le type d'étape"""
        if self.place:
            return self.place.name
        elif self.hotel:
            return self.hotel.name
        elif self.city:
            return self.city.name
        else:
            return self.custom_name or "Étape sans nom"


class ItineraryLike(models.Model):
    """Système de likes pour les itinéraires"""
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['itinerary', 'user']  # Un utilisateur ne peut liker qu'une fois
        verbose_name = "Like d'itinéraire"
        verbose_name_plural = "Likes d'itinéraires"
    
    def __str__(self):
        return f"{self.user.username} aime {self.itinerary.name}"


class ItineraryShare(models.Model):
    """Historique des partages d'itinéraires"""
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='shares')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shared_at = models.DateTimeField(auto_now_add=True)
    share_method = models.CharField(max_length=50, blank=True, null=True)  # email, social, etc.
    
    def __str__(self):
        return f"{self.itinerary.name} partagé par {self.user.username if self.user else 'anonyme'}"


class Route(models.Model):
    """Ancien modèle Route - conservé pour la compatibilité"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name