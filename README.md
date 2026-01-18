# Tourisme Maroc - Coupe du Monde 2030

Projet Django de promotion touristique du Maroc pour la Coupe du Monde 2030. Développé par une équipe de 4 étudiants.

## Équipe
- **Membre 1** : Hamza Layachi : Backend Core, villes, Coupe du Monde
- **Membre 2** : Ibtissam Ainzura : Hôtels et lieux touristiques
- **Membre 3** : Imane El assioui : Itinéraires et routes
- **Membre 4** : Amina chetti : Utilisateurs et authentification

## Installation:
git clone https://github.com/h1mza07/Digital-creativity.git
cd Digital-creativity
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
## Structure:
cities/ : Villes marocaines (Hamza Layachi)

worldcup2030/ : Coupe du Monde (Hamza Layachi)

hotels/ : Hôtels Ibtissam Ainzura)

routes/ : Itinéraires (Imane El assioui)

users/ : Authentification (Amina Chetti)

## Technologies:
Django 4.2.7, Python

Bootstrap 5, Leaflet

SQLite, i18n (FR/EN)

Accès : http://127.0.0.1:8000 | Admin : http://127.0.0.1:8000/admin


## 👩‍💻 Contributions de EL Assioui Imane

- Création de la page **“À propos”** avec présentation de l’équipe
- Implémentation du **compteur de vues global** sur la page d’accueil
- Ajout du **filtre par note (1 à 5 étoiles)** dans la liste des itinéraires
- Intégration du **thème sombre/bascule** avec persistance
- Amélioration de l’**accessibilité** et du **SEO**