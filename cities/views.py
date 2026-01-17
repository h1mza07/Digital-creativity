from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import City

def home_page(request):
    return render(request, 'home.html')

def city_list(request):
    cities = City.objects.all()
    
    # HTML avec CSS INTERNE amélioré
    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Villes Marocaines - Maroc Tourisme 2030</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                padding: 20px;
                min-height: 100vh;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            header {
                text-align: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 3px solid #006233;
            }
            h1 {
                color: #006233;
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #666;
                font-size: 1.2rem;
            }
            .stats {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
                font-size: 1.1rem;
                color: #006233;
                border-left: 5px solid #006233;
            }
            .city-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .city-card {
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.08);
                transition: all 0.3s ease;
                border: 1px solid #eaeaea;
            }
            .city-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0,0,0,0.15);
            }
            .card-header {
                background: #006233;
                color: white;
                padding: 20px;
            }
            .card-body {
                padding: 25px;
            }
            .city-name {
                font-size: 1.5rem;
                color: #006233;
                margin-bottom: 10px;
            }
            .city-desc {
                color: #555;
                line-height: 1.6;
                margin-bottom: 15px;
                font-size: 0.95rem;
            }
            .city-info {
                display: flex;
                justify-content: space-between;
                color: #777;
                font-size: 0.9rem;
                margin-bottom: 20px;
                padding-top: 15px;
                border-top: 1px solid #eee;
            }
            .btn {
                display: inline-block;
                background: #006233;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: background 0.3s;
                border: none;
                cursor: pointer;
                font-size: 1rem;
            }
            .btn:hover {
                background: #004d26;
            }
            .back-link {
                display: inline-block;
                margin-top: 30px;
                color: #006233;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.1rem;
            }
            .worldcup-badge {
                background: #ff6b00;
                color: white;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
                margin-left: 10px;
                font-weight: bold;
            }
            .nav-bar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 30px;
                padding-bottom: 15px;
                border-bottom: 2px solid #eee;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: bold;
                color: #006233;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="nav-bar">
                <a href="/" class="logo">🇲🇦 Maroc Tourisme <span class="worldcup-badge">CM 2030</span></a>
                <a href="/" class="btn">Accueil</a>
            </div>
            
            <header>
                <h1>Villes Marocaines</h1>
                <p class="subtitle">Découvrez les principales villes du Maroc pour la Coupe du Monde 2030</p>
            </header>
            
            <div class="stats">
                🏙️ <strong>""" + str(cities.count()) + """ villes</strong> disponibles à la découverte
            </div>
            
            <div class="city-grid">
    """
    
    for city in cities:
        html += f"""
                <div class="city-card">
                    <div class="card-header">
                        <h3>{city.name}</h3>
                    </div>
                    <div class="card-body">
                        <div class="city-name">{city.name}</div>
                        <p class="city-desc">{city.description[:120]}...</p>
                        <div class="city-info">
                            <span>👥 {city.population} habitants</span>
                            <span>📍 {city.latitude}, {city.longitude}</span>
                        </div>
                        <a href="/cities/{city.slug}/" class="btn">Explorer cette ville →</a>
                    </div>
                </div>
        """
    
    html += """
            </div>
            
            <a href="/" class="back-link">← Retour à la page d'accueil</a>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)

def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    
    # HTML avec design moderne
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{city.name} - Maroc Tourisme 2030</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                padding: 20px;
                min-height: 100vh;
            }}
            .container {{
                max-width: 1000px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }}
            .nav-bar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 2px solid #eee;
            }}
            .logo {{
                font-size: 1.8rem;
                font-weight: bold;
                color: #006233;
                text-decoration: none;
            }}
            .btn {{
                display: inline-block;
                background: #006233;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: background 0.3s;
            }}
            .btn:hover {{ background: #004d26; }}
            .btn-secondary {{
                background: #6c757d;
                margin-left: 10px;
            }}
            .city-header {{
                text-align: center;
                margin-bottom: 40px;
            }}
            h1 {{
                color: #006233;
                font-size: 2.8rem;
                margin-bottom: 15px;
            }}
            .city-description {{
                font-size: 1.2rem;
                line-height: 1.8;
                color: #444;
                margin-bottom: 30px;
                padding: 20px;
                background: #f8f9fa;
                border-radius: 10px;
                border-left: 5px solid #006233;
            }}
            .info-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin: 40px 0;
            }}
            .info-card {{
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                border: 1px solid #eaeaea;
            }}
            .info-card h3 {{
                color: #006233;
                margin-bottom: 15px;
                padding-bottom: 10px;
                border-bottom: 2px solid #eee;
            }}
            .info-item {{
                margin: 15px 0;
                display: flex;
                align-items: center;
            }}
            .info-icon {{
                font-size: 1.5rem;
                margin-right: 15px;
                color: #006233;
            }}
            .map-placeholder {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 300px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 1.3rem;
                margin: 30px 0;
            }}
            .worldcup-badge {{
                background: #ff6b00;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9rem;
                margin-left: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="nav-bar">
                <a href="/" class="logo">🇲🇦 Maroc Tourisme <span class="worldcup-badge">CM 2030</span></a>
                <div>
                    <a href="/cities/" class="btn">← Retour aux villes</a>
                    <a href="/" class="btn btn-secondary">Accueil</a>
                </div>
            </div>
            
            <div class="city-header">
                <h1>{city.name}</h1>
            </div>
            
            <div class="city-description">
                {city.description}
            </div>
            
            <div class="info-grid">
                <div class="info-card">
                    <h3>📊 Informations</h3>
                    <div class="info-item">
                        <span class="info-icon">👥</span>
                        <div>
                            <strong>Population:</strong> {city.population} habitants
                        </div>
                    </div>
                    <div class="info-item">
                        <span class="info-icon">📍</span>
                        <div>
                            <strong>Coordonnées GPS:</strong><br>
                            Latitude: {city.latitude}<br>
                            Longitude: {city.longitude}
                        </div>
                    </div>
                </div>
                
                <div class="info-card">
                    <h3>🗺️ Localisation</h3>
                    <div class="map-placeholder">
                        Carte interactive de {city.name}<br>
                        (Leaflet JS à intégrer)
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="/cities/" class="btn">← Voir toutes les villes</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)