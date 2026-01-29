# hotels/models.py
from django.db import models
from cities.models import City

class Hotel(models.Model) : 
    description = models.TextField()
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=300)
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    def __str__(self):
        return self.name