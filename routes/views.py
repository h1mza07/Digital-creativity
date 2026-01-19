from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Itinerary, Comment, VisitCount

def home(request):
    # Clé de cache unique pour cette session ou IP
    visitor_key = f"visitor_{request.session.session_key or request.META.get('REMOTE_ADDR', 'unknown')}"
    
    if not cache.get(visitor_key):
        # Première visite de cet utilisateur / incrémenter
        visit, created = VisitCount.objects.get_or_create(id=1)
        visit.total_visits += 1
        visit.save(update_fields=['total_visits'])
        # Marquer comme vu pendant 1 heure
        cache.set(visitor_key, True, timeout=3600)
    
    total_visits = VisitCount.objects.get(id=1).total_visits
    return render(request, 'routes/home.html', {'total_visits': total_visits})

def about(request):
    team_members = [
        {
            'name': 'Hamza Layachi',
            'role': 'Chef de projet & Core Backend',
            'responsibilities': ['Initialisation du projet', 'Modèles: City, HostCity']
        },
        {
            'name': 'Ibtissam Ainzura',
            'role': 'Lieux touristiques & Cartographie',
            'responsibilities': ['App: places', 'Intégration Leaflet']
        },
        {
            'name': 'EL Assioui Imane',
            'role': 'Hôtels & Itinéraires',
            'responsibilities': ['Apps: hotels, routes', 'Modèles: Hotel, Itinerary']
        },
        {
            'name': 'Amina Chetti',
            'role': 'Utilisateurs, Sécurité & UX',
            'responsibilities': ['App: users', 'Authentification', 'UX']
        }
    ]
    return render(request, 'routes/about.html', {'team_members': team_members})

def itinerary_list(request):
    query = request.GET.get('q')
    itineraries = Itinerary.objects.all()

    if query:
        itineraries = itineraries.filter(title__icontains=query)

    return render(request, 'routes/itinerary_list.html', {
        'itineraries': itineraries,
        'query': query
    })
    
    return render(request, 'routes/itinerary_list.html', context)

def itinerary_search(request):
    message = "Recherche d'itinéraires (à remplacer plus tard par une vraie recherche)."
    return render(request, 'routes/search.html', {'message': message})

def profile_view(request):
    return render(request, 'routes/profile.html')

def itinerary_detail(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    comments = itinerary.comments.all().order_by('-created_at')
    return render(request, 'routes/itinerary_detail.html', {
        'itinerary': itinerary,
        'comments': comments,
    })

@require_POST
def add_comment(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    author = request.POST.get('author', 'Anonyme').strip() or 'Anonyme'
    text = request.POST.get('text', '').strip()
    
    if text:
        Comment.objects.create(
            itinerary=itinerary,
            author=author,
            text=text
        )
        messages.success(request, "Votre commentaire a été ajouté avec succès !")
    else:
        messages.error(request, "Le commentaire ne peut pas être vide.")
    
    return redirect ('itinerary_detail', itinerary_id=itinerary_id)