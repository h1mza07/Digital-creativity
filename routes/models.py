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


class VisitCount(models.Model):
    total_visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Total des visites : {self.total_visits}"