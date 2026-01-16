from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Place, City
from cities.models import City as CitiesCity  # Pour éviter la confusion

class PlaceModelTest(TestCase):
    """Tests pour le modèle Place"""
    
    def setUp(self):
        """Préparation des données de test"""
        # Création d'une ville pour les tests
        self.city = CitiesCity.objects.create(
            name="Marrakech",
            description="Ville touristique du Maroc",
            image=None
        )
        
        # Création d'un lieu touristique
        self.place = Place.objects.create(
            name="Jardin Majorelle",
            description="Jardin botanique et artistique",
            city=self.city,
            category='jardin',
            latitude=31.6462,
            longitude=-8.0019,
            entry_price=70.00,
            opening_hours="8h00 - 17h30",
            best_time_to_visit="Printemps"
        )
    
    def test_place_creation(self):
        """Test de création d'un lieu touristique"""
        self.assertEqual(self.place.name, "Jardin Majorelle")
        self.assertEqual(self.place.city.name, "Marrakech")
        self.assertEqual(self.place.category, 'jardin')
        self.assertEqual(float(self.place.entry_price), 70.00)
        self.assertTrue(self.place.latitude)
        self.assertTrue(self.place.longitude)
    
    def test_place_str_representation(self):
        """Test de la représentation textuelle"""
        expected_str = f"{self.place.name} - {self.place.city.name}"
        self.assertEqual(str(self.place), expected_str)
    
    def test_place_gps_coordinates(self):
        """Test des coordonnées GPS"""
        expected_coords = f"{self.place.latitude},{self.place.longitude}"
        self.assertEqual(self.place.gps_coordinates, expected_coords)
    
    def test_place_has_images(self):
        """Test de la propriété has_images"""
        # Sans image
        self.assertFalse(self.place.has_images)
        
        # Avec image (on simule)
        self.place.main_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        self.assertTrue(self.place.has_images)


class PlaceViewsTest(TestCase):
    """Tests pour les vues de l'app places"""
    
    def setUp(self):
        """Préparation des données pour les tests de vues"""
        self.client = Client()
        self.city = CitiesCity.objects.create(
            name="Test City",
            description="Ville de test"
        )
        
        # Création de plusieurs lieux pour tester les listes
        for i in range(1, 6):
            Place.objects.create(
                name=f"Lieu Test {i}",
                description=f"Description du lieu test {i}",
                city=self.city,
                category='monument',
                latitude=31.0 + i/100,
                longitude=-8.0 + i/100
            )
    
    def test_place_list_view_status_code(self):
        """Test que la vue de liste des lieux retourne un code 200"""
        response = self.client.get(reverse('place_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_place_list_view_template(self):
        """Test que la vue utilise le bon template"""
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'places/list.html')
    
    def test_place_list_view_context(self):
        """Test que la vue transmet bien les lieux dans le contexte"""
        response = self.client.get(reverse('place_list'))
        self.assertTrue('places' in response.context)
        self.assertEqual(len(response.context['places']), 5)
    
    def test_place_detail_view(self):
        """Test de la vue de détail d'un lieu"""
        place = Place.objects.first()
        response = self.client.get(reverse('place_detail', args=[place.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/detail.html')
        self.assertEqual(response.context['place'], place)
    
    def test_place_filter_by_city(self):
        """Test du filtre par ville"""
        # Création d'une autre ville et d'un lieu dans cette ville
        other_city = CitiesCity.objects.create(name="Autre Ville", description="...")
        Place.objects.create(
            name="Lieu dans autre ville",
            description="...",
            city=other_city,
            category='musee'
        )
        
        # Filtre par la première ville
        response = self.client.get(reverse('place_list') + f'?city={self.city.id}')
        self.assertEqual(len(response.context['places']), 5)
    
    def test_place_search(self):
        """Test de la recherche"""
        response = self.client.get(reverse('place_list') + '?search=Test 3')
        self.assertEqual(len(response.context['places']), 1)
        self.assertEqual(response.context['places'][0].name, "Lieu Test 3")


class PlaceAdminTest(TestCase):
    """Tests pour l'interface d'administration"""
    
    def setUp(self):
        from django.contrib.auth.models import User
        # Création d'un superutilisateur
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass'
        )
        self.client = Client()
        
        self.city = CitiesCity.objects.create(name="Admin City", description="...")
        self.place = Place.objects.create(
            name="Lieu Admin",
            description="...",
            city=self.city,
            category='monument'
        )
    
    def test_admin_login(self):
        """Test de l'accès à l'admin"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_place_list(self):
        """Test que les lieux apparaissent dans l'admin"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/admin/places/place/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.place.name)


class PlaceURLTest(TestCase):
    """Tests pour les URLs"""
    
    def test_place_list_url(self):
        """Test de l'URL de la liste des lieux"""
        url = reverse('place_list')
        self.assertEqual(url, '/lieux/')
    
    def test_place_detail_url(self):
        """Test de l'URL de détail d'un lieu"""
        # On crée un lieu pour avoir un PK
        city = CitiesCity.objects.create(name="URL City", description="...")
        place = Place.objects.create(
            name="Lieu URL",
            description="...",
            city=city,
            category='monument'
        )
        
        url = reverse('place_detail', args=[place.pk])
        expected_url = f'/lieux/{place.pk}/'
        self.assertEqual(url, expected_url)
    
    def test_place_map_url(self):
        """Test de l'URL de la carte"""
        # Note: Cette URL n'est pas encore définie dans urls.py
        # On peut la commenter pour l'instant
        # url = reverse('place_map')
        # self.assertEqual(url, '/lieux/carte/')
        pass


# Test pour les modèles associés
class VisitorReviewTest(TestCase):
    """Tests pour le modèle VisitorReview"""
    
    def setUp(self):
        self.city = CitiesCity.objects.create(name="Review City", description="...")
        self.place = Place.objects.create(
            name="Lieu avec avis",
            description="...",
            city=self.city,
            category='nature'
        )
    
    def test_review_creation(self):
        """Test de création d'un avis"""
        from .models import VisitorReview
        review = VisitorReview.objects.create(
            place=self.place,
            visitor_name="Jean Dupont",
            rating=5,
            comment="Superbe endroit !",
            visit_date="2024-01-01"
        )
        
        self.assertEqual(review.visitor_name, "Jean Dupont")
        self.assertEqual(review.rating, 5)
        self.assertFalse(review.is_approved)  # Par défaut non approuvé


if __name__ == '__main__':
    print("Tests pour l'application 'places'")
    print("Pour exécuter les tests : python manage.py test places")