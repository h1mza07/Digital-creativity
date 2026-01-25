# hotels/models.py
from django.db import models
from cities.models import City

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=3,
        help_text="Note sur 5 étoiles"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Prix par nuit (MAD)")
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    def __str__(self):
        return self.name