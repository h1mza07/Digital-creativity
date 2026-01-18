from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Itinerary, Comment, VisitCount

def home(request):
    visit, created = VisitCount.objects.get_or_create(id=1)
    visit.total_visits += 1
    visit.save(update_fields=['total_visits'])
    return render(request, 'routes/home.html', {'total_visits': visit.total_visits})

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
    rating_filter = request.GET.get('rating')
    itineraries = Itinerary.objects.all()

    if rating_filter:
        itineraries = itineraries.filter(rating__gte=int(rating_filter))

    context = {
        'itineraries': itineraries,
        'selected_rating': rating_filter or '',
    }
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
    
    return redirect('itinerary_detail', itinerary_id=itinerary_id