from django.db import models
from cities.models import City

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stars = models.IntegerField(choices=[(i, f"{i} étoile{'s' if i > 1 else ''}") for i in range(1, 6)])
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stars}★) - {self.city.name}"