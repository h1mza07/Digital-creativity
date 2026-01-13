from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username} - {self.place_name}"
