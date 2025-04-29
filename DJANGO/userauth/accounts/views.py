from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'netflix-register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'netflix-login.html')

def logout_view(request):
    logout(request)
    return redirect('landing')

def landing_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'landing.html')

@login_required
def home_view(request):
    # Import here to avoid circular imports
    from movies.models import Movie, Genre, Mood

    # Get some sample data for the dashboard
    recent_movies = Movie.objects.order_by('-year')[:4]
    top_rated_movies = Movie.objects.order_by('-imdb_rating')[:4]
    genres = Genre.objects.all()[:6]
    moods = Mood.objects.all()

    context = {
        'recent_movies': recent_movies,
        'top_rated_movies': top_rated_movies,
        'genres': genres,
        'moods': moods,
    }

    return render(request, 'netflix-home.html', context)
