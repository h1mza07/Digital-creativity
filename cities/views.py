from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import City

def home_page(request):
    return render(request, 'home.html')

def city_list(request):
    cities = City.objects.all()
    
    # CODE GARANTI SANS PAGE BLANCHE
    html = """
    <html>
    <body style="background: #f0f0f0; padding: 20px; font-family: Arial;">
        <h1 style="color: #006233;">VILLES MAROCAINES</h1>
        <p>Nombre de villes: """ + str(cities.count()) + """</p>
        <ul style="list-style: none; padding: 0;">
    """
    
    for city in cities:
        html += f"""
        <li style="background: white; margin: 10px 0; padding: 15px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1)">
            <strong>{city.name}</strong><br>
            {city.description[:100]}...
            <br><small>Population: {city.population}</small>
            <br><a href="/cities/{city.slug}/" style="color: #006233;">Voir détails</a>
        </li>
        """
    
    html += """
        </ul>
        <p><a href="/" style="color: #006233;">← Retour à l'accueil</a></p>
    </body>
    </html>
    """
    
    return HttpResponse(html)

def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    
    # HTML DIRECT pour éviter page blanche
    html = f"""
    <html>
    <body style="background: #f0f0f0; padding: 20px; font-family: Arial;">
        <h1 style="color: #006233;">{city.name}</h1>
        <p>{city.description}</p>
        <p><strong>Population:</strong> {city.population}</p>
        <p><strong>Coordonnées:</strong> {city.latitude}, {city.longitude}</p>
        <p><a href="/cities/" style="color: #006233;">← Retour aux villes</a></p>
    </body>
    </html>
    """
    
    return HttpResponse(html)