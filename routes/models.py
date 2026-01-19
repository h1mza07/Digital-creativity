from django.db import models
from django.contrib.auth.models import User
from places.models import Place
from hotels.models import Hotel
from cities.models import City

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