from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Place(models.Model):
    """Modèle pour les lieux touristiques du Maroc"""
    
    # Choix des catégories
    CATEGORY_MONUMENT = 'monument'
    CATEGORY_MUSEUM = 'musee'
    CATEGORY_NATURE = 'nature'
    CATEGORY_BEACH = 'plage'
    CATEGORY_MARKET = 'souk'
    CATEGORY_GARDEN = 'jardin'
    CATEGORY_RELIGIOUS = 'mosquee'
    CATEGORY_FORTRESS = 'kasbah'
    
    CATEGORY_CHOICES = [
        (CATEGORY_MONUMENT, _('Monument historique')),
        (CATEGORY_MUSEUM, _('Musée')),
        (CATEGORY_NATURE, _('Site naturel')),
        (CATEGORY_BEACH, _('Plage')),
        (CATEGORY_MARKET, _('Marché traditionnel (Souk)')),
        (CATEGORY_GARDEN, _('Jardin/parc')),
        (CATEGORY_RELIGIOUS, _('Lieu religieux')),
        (CATEGORY_FORTRESS, _('Forteresse/Kasbah')),
    ]
    
    # Champs principaux
    name = models.CharField(
        max_length=200, 
        verbose_name=_("Nom du lieu"),
        help_text=_("Ex: Kasbah de Tanger, Grottes d'Hercule")
    )
    
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Décrivez le lieu en 2-3 phrases")
    )
    
    city = models.ForeignKey(
        'cities.City',  # Référence à l'application cities
        on_delete=models.CASCADE,
        verbose_name=_("Ville"),
        related_name='places',
        help_text=_("Ville marocaine où se trouve le lieu")
    )
    
    # Informations pratiques
    address = models.CharField(
        max_length=300, 
        verbose_name=_("Adresse"),
        blank=True, 
        null=True
    )
    
    entry_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name=_("Prix d'entrée (DH)"),
        blank=True, 
        null=True,
        help_text=_("Prix en dirhams marocains")
    )
    
    opening_hours = models.CharField(
        max_length=100, 
        verbose_name=_("Horaires d'ouverture"),
        blank=True, 
        null=True,
        help_text=_("Ex: 9h00 - 18h00, Fermé le lundi")
    )
    
    best_time_to_visit = models.CharField(
        max_length=100, 
        verbose_name=_("Meilleure période"),
        blank=True, 
        null=True,
        help_text=_("Ex: Printemps, Été, Toute l'année")
    )
    
    # Catégorie et localisation
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES,
        default=CATEGORY_MONUMENT,
        verbose_name=_("Catégorie")
    )
    
    latitude = models.FloatField(
        verbose_name=_("Latitude"),
        blank=True, 
        null=True,
        help_text=_("Coordonnée GPS pour la carte")
    )
    
    longitude = models.FloatField(
        verbose_name=_("Longitude"),
        blank=True, 
        null=True,
        help_text=_("Coordonnée GPS pour la carte")
    )
    
    # Images
    main_image = models.ImageField(
        upload_to='places/main/',
        verbose_name=_("Image principale"),
        blank=True, 
        null=True
    )
    
    additional_images = models.TextField(
        verbose_name=_("URLs d'images supplémentaires"),
        blank=True, 
        null=True,
        help_text=_("URLs séparées par des virgules")
    )
    
    # Métadonnées
    is_featured = models.BooleanField(
        default=False,
        verbose_name=_("Mis en avant"),
        help_text=_("Afficher en priorité sur le site")
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création")
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Dernière modification")
    )
    
    class Meta:
        verbose_name = _("Lieu touristique")
        verbose_name_plural = _("Lieux touristiques")
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['city', 'category']),
            models.Index(fields=['is_featured']),
        ]
    
    def __str__(self):
        """Représentation textuelle du lieu"""
        return f"{self.name} - {self.city.name if self.city else 'Ville inconnue'}"
    
    def clean(self):
        """Validation des données"""
        super().clean()
        errors = {}
        
        # Validation des coordonnées GPS
        if self.latitude and not (-90 <= self.latitude <= 90):
            errors['latitude'] = _("La latitude doit être entre -90 et 90")
        
        if self.longitude and not (-180 <= self.longitude <= 180):
            errors['longitude'] = _("La longitude doit être entre -180 et 180")
        
        if self.entry_price and self.entry_price < 0:
            errors['entry_price'] = _("Le prix ne peut pas être négatif")
        
        if errors:
            raise ValidationError(errors)
    
    def get_absolute_url(self):
        """URL pour accéder au détail du lieu"""
        from django.urls import reverse
        return reverse('place_detail', kwargs={'pk': self.pk})
    
    @property
    def gps_coordinates(self):
        """Propriété pour les coordonnées GPS formatées"""
        if self.latitude and self.longitude:
            return f"{self.latitude},{self.longitude}"
        return None
    
    @property
    def has_images(self):
        """Vérifie si le lieu a des images"""
        return bool(self.main_image or self.additional_images)
    
    def save(self, *args, **kwargs):
        """Surcharge de la méthode save pour ajouter des validations"""
        self.clean()
        super().save(*args, **kwargs)


class VisitorReview(models.Model):
    """Modèle pour les avis des visiteurs sur les lieux"""
    
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_("Lieu")
    )
    
    visitor_name = models.CharField(
        max_length=100, 
        verbose_name=_("Nom du visiteur")
    )
    
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=3,
        verbose_name=_("Note")
    )
    
    comment = models.TextField(
        verbose_name=_("Commentaire"),
        max_length=500
    )
    
    visit_date = models.DateField(
        verbose_name=_("Date de visite")
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de publication")
    )
    
    is_approved = models.BooleanField(
        default=False,
        verbose_name=_("Approuvé"),
        help_text=_("L'avis doit être approuvé avant publication")
    )
    
    class Meta:
        verbose_name = _("Avis visiteur")
        verbose_name_plural = _("Avis visiteurs")
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Avis de {self.visitor_name} sur {self.place.name}"


class PlaceImage(models.Model):
    """Modèle pour les images supplémentaires des lieux"""
    
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='place_images',
        verbose_name=_("Lieu")
    )
    
    image = models.ImageField(
        upload_to='places/gallery/',
        verbose_name=_("Image")
    )
    
    caption = models.CharField(
        max_length=200, 
        verbose_name=_("Légende"),
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Ordre d'affichage")
    )
    
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date d'upload")
    )
    
    class Meta:
        verbose_name = _("Image de lieu")
        verbose_name_plural = _("Images de lieu")
        ordering = ['order', 'uploaded_at']
    
    def __str__(self):
        return f"Image pour {self.place.name}"
