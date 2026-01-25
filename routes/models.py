from django.db import models
from django.contrib.auth.models import User
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