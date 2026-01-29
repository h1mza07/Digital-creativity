# routes/models.py
from django.db import models
from django.conf import settings
from hotels.models import Hotel
from places.models import Stadium, Place
from cities.models import City

class Itinerary(models.Model):
    """Itinéraire entre un hôtel et un stade"""
    
    DIFFICULTY_CHOICES = [
        ('facile', 'Facile'),
        ('moyen', 'Moyen'),
        ('difficile', 'Difficile'),
    ]
    
    # 🔑 Relations principales
    hotel = models.ForeignKey(
        Hotel, 
        on_delete=models.CASCADE, 
        related_name='itineraries',
        null=True,
        blank=True,
        help_text="Hôtel de départ"
    )
    stadium = models.ForeignKey(
        Stadium, 
        on_delete=models.CASCADE, 
        related_name='itineraries',
        null=True,
        blank=True,
        help_text="Stade d'arrivée"
    )
    
    # Informations générales
    title = models.CharField(max_length=200, default="Itinéraire sans nom")
    description = models.TextField(blank=True)
    duration_days = models.IntegerField(default=1)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='facile')
    city = models.CharField(max_length=100, default="Marrakech")
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='itineraries'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 🏨 Informations hôtel (pour rétrocompatibilité)
    hotel_name = models.CharField(max_length=200, blank=True)
    hotel_rating = models.IntegerField(default=0)
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    hotel_address = models.CharField(max_length=300, blank=True)
    
    # 🏟 Informations stade (pour rétrocompatibilité)
    stadium_name = models.CharField(max_length=200, blank=True)
    stadium_address = models.CharField(max_length=300, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    # 📋 Informations pratiques
    best_season = models.CharField(max_length=100, default="Toute l'année")
    required_equipment = models.TextField(blank=True, default="Aucun équipement spécial requis")
    contact_info = models.CharField(max_length=200, blank=True, default="Non disponible")
    
    # 💰 Prix total
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # 🔧 Méthodes utilitaires
    def save(self, *args, **kwargs):
        """Synchronise les champs textuels avec les relations"""
        if self.hotel:
            self.hotel_name = self.hotel.name
            self.hotel_rating = getattr(self.hotel, 'rating', 0)
            self.hotel_price = getattr(self.hotel, 'price', 0)
            self.hotel_address = getattr(self.hotel, 'address', '')
            self.city = getattr(self.hotel.city, 'name', 'Marrakech')
        
        if self.stadium:
            self.stadium_name = self.stadium.name
            self.stadium_address = getattr(self.stadium, 'address', '')
            self.distance = getattr(self.stadium, 'distance', 0)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.hotel and self.stadium:
            return f"{self.hotel.name} → {self.stadium.name}"
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Itinéraire"
        verbose_name_plural = "Itinéraires"


class Route(models.Model):
    """Route depuis un hôtel vers un stade"""
    
    TRANSPORT_MODE_CHOICES = [
        ('taxi', 'Taxi'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('voiture', 'Voiture'),
        ('marche', 'À pied'),
    ]
    
    # 🔑 Relations
    hotel = models.ForeignKey(
        Hotel, 
        on_delete=models.CASCADE, 
        related_name='routes',
        help_text="Hôtel de départ"
    )
    stadium = models.ForeignKey(
        Stadium, 
        on_delete=models.CASCADE, 
        related_name='routes',
        null=True,
        blank=True,
        help_text="Stade d'arrivée"
    )
    
    # Informations générales
    name = models.CharField(max_length=200)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    
    # 🏟 Informations stade (pour rétrocompatibilité)
    stadium_name = models.CharField(max_length=200, blank=True)
    stadium_address = models.CharField(max_length=300, blank=True)
    
    # 📍 Coordonnées GPS
    latitude_start = models.FloatField(default=0.0)
    longitude_start = models.FloatField(default=0.0)
    latitude_end = models.FloatField(default=0.0)
    longitude_end = models.FloatField(default=0.0)
    
    # 📊 Statistiques
    distance_km = models.FloatField(help_text="Distance en kilomètres")
    estimated_time_min = models.IntegerField(help_text="Temps estimé en minutes")
    
    # 🚌 Mode de transport
    transport_mode = models.CharField(
        max_length=50, 
        choices=TRANSPORT_MODE_CHOICES,
        default='taxi'
    )
    
    # 💰 Prix
    price_estimate = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Prix estimé du trajet"
    )
    
    def save(self, *args, **kwargs):
        """Synchronise les champs textuels avec les relations"""
        if self.stadium:
            self.stadium_name = self.stadium.name
            self.stadium_address = getattr(self.stadium, 'address', '')
            self.to_location = self.stadium.name
        
        if self.hotel:
            self.from_location = self.hotel.name
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.hotel.name} → {self.stadium_name or self.to_location}"
    
    class Meta:
        ordering = ['hotel', 'stadium']
        verbose_name = "Route"
        verbose_name_plural = "Routes"


class CustomItinerary(models.Model):
    """Itinéraire personnalisé créé par un utilisateur"""
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='custom_itineraries'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, help_text="Rendre l'itinéraire public")
    views_count = models.PositiveIntegerField(default=0, editable=False)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Itinéraire personnalisé"
        verbose_name_plural = "Itinéraires personnalisés"


class ItineraryStop(models.Model):
    """Étape d'un itinéraire personnalisé"""
    
    itinerary = models.ForeignKey(
        CustomItinerary, 
        related_name='stops', 
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(help_text="Ordre de l'étape")
    
    # 🔑 Relations (une seule doit être remplie)
    place = models.ForeignKey(
        Place, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='itinerary_stops'
    )
    hotel = models.ForeignKey(
        Hotel, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='itinerary_stops'
    )
    city = models.ForeignKey(
        City, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='itinerary_stops'
    )
    
    # 📍 Coordonnées optionnelles
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    # 📝 Informations supplémentaires
    description = models.TextField(blank=True, help_text="Description de l'étape")
    duration_hours = models.FloatField(
        null=True, 
        blank=True, 
        help_text="Durée estimée en heures"
    )
    is_optional = models.BooleanField(default=False, help_text="Étape facultative")
    
    def __str__(self):
        if self.place:
            return f"Place: {self.place.name}"
        elif self.hotel:
            return f"Hotel: {self.hotel.name}"
        else:
            return f"City: {self.city.name}"
    
    class Meta:
        ordering = ['order']
        verbose_name = "Étape d'itinéraire"
        verbose_name_plural = "Étapes d'itinéraire"