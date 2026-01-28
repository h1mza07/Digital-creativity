from django.db import models
from django.conf import settings
from hotels.models import Hotel
from places.models import Place
from cities.models import City

class Itinerary(models.Model):
    DIFFICULTY_CHOICES = [
        ('facile', 'Facile'),
        ('moyen', 'Moyen'),
        ('difficile', 'Difficile'),
    ]
    
    title = models.CharField(max_length=200, default="Itinéraire sans nom")
    description = models.TextField()
    duration_days = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    city = models.CharField(max_length=100, default="Marrakech")
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='itineraries')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Informations hôtel
    hotel_name = models.CharField(max_length=200)
    hotel_rating = models.IntegerField()
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_address = models.CharField(max_length=300)
    
    # Informations stade
    stadium_name = models.CharField(max_length=200)
    stadium_address = models.CharField(max_length=300)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Informations pratiques
    best_season = models.CharField(max_length=100, default="Toute l'année")
    required_equipment = models.TextField()
    contact_info = models.CharField(max_length=200)
    
    # Prix total
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title

class Route(models.Model):
    """Route depuis un hôtel vers un stade"""
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='routes')
    name = models.CharField(max_length=200)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    stadium_name = models.CharField(max_length=200)
    stadium_address = models.CharField(max_length=300)
    distance_km = models.FloatField()
    estimated_time_min = models.IntegerField()
    transport_mode = models.CharField(max_length=50, default='Taxi')
    price_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    latitude_start = models.FloatField(default=0.0)
    longitude_start = models.FloatField(default=0.0)
    latitude_end = models.FloatField()
    longitude_end = models.FloatField()
    
    def __str__(self):
        return f"{self.hotel.name} → {self.stadium_name}"

class CustomItinerary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class ItineraryStop(models.Model):
    itinerary = models.ForeignKey(CustomItinerary, related_name='stops', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        if self.place:
            return f"Place: {self.place.name}"
        elif self.hotel:
            return f"Hotel: {self.hotel.name}"
        else:
            return f"City: {self.city.name}"