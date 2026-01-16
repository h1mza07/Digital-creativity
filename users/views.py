from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Favorite

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'users/login.html')


@login_required
def profile(request):
    profile = request.user.profile
    favorites = request.user.favorites.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile.html', {
        'form': form,
        'favorites': favorites
    })


@login_required
def add_favorite(request, place_name):
    Favorite.objects.create(user=request.user, place_name=place_name)
    return redirect('profile')


@login_required
def remove_favorite(request, fav_id):
    Favorite.objects.filter(id=fav_id, user=request.user).delete()
    return redirect('profile')
