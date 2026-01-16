 from django.apps import AppConfig

class PlacesConfig(AppConfig):
    """
    Configuration de l'application 'places' pour la gestion des lieux touristiques.
    Développée par Ibtissam Ainzura (Membre 2) - Projet Maroc Tourisme 2030.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'places'
    verbose_name = "🎯 Lieux Touristiques"
    
    def ready(self):
        """
        Méthode exécutée quand l'application est chargée.
        On pourrait y ajouter des signaux ou des configurations initiales.
        """
        # Pour l'instant, on ne fait rien de spécial
        # Plus tard, on pourrait ajouter :
        # - Des signaux pour les images
        # - Des permissions par défaut
        # - Des groupes d'administration
        pass
    
    class Meta:
        """Métadonnées supplémentaires (optionnel)"""
        app_label = 'places'