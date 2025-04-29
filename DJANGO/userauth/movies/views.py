from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Genre, Language, Mood, UserRating
from .forms import MoviePreferenceForm, MovieRatingForm
from .recommendation import get_recommendations, get_popular_movies, get_similar_movies

@login_required
def preference_form(request):
    """View for user to input their movie preferences"""
    if request.method == 'POST':
        form = MoviePreferenceForm(request.POST)
        if form.is_valid():
            form.save_preferences(request.user)
            mood = form.cleaned_data.get('mood')

            # Redirect to recommendations with mood parameter if provided
            if mood:
                return redirect('movie_recommendations', mood_id=mood.id)
            else:
                return redirect('movie_recommendations')
    else:
        form = MoviePreferenceForm()

    return render(request, 'movies/netflix-preference-form.html', {'form': form})

@login_required
def movie_recommendations(request, mood_id=None):
    """View to display movie recommendations"""
    mood = None
    if mood_id:
        mood = get_object_or_404(Mood, id=mood_id)

    # Get recommendations based on user preferences and mood
    recommended_movies = get_recommendations(request.user, mood=mood)

    # If no recommendations based on preferences, show popular movies
    if not recommended_movies:
        recommended_movies = get_popular_movies()
        messages.info(request, "We don't have enough information about your preferences yet. Here are some popular movies you might enjoy!")

    # Get all moods for the mood selector
    moods = Mood.objects.all()

    context = {
        'movies': recommended_movies,
        'mood': mood,
        'moods': moods,
    }

    return render(request, 'movies/netflix-recommendations.html', context)

@login_required
def movie_detail(request, movie_id):
    """View to display movie details and allow rating"""
    movie = get_object_or_404(Movie, id=movie_id)
    similar_movies = get_similar_movies(movie_id)

    # Handle rating form
    if request.method == 'POST':
        form = MovieRatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']

            # Create or update user rating
            rating, created = UserRating.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={'rating': rating_value}
            )

            if created:
                messages.success(request, f"Thank you for rating '{movie.title}'!")
            else:
                messages.success(request, f"Your rating for '{movie.title}' has been updated!")

            return redirect('movie_detail', movie_id=movie_id)
    else:
        # Check if user has already rated this movie
        try:
            user_rating = UserRating.objects.get(user=request.user, movie=movie)
            form = MovieRatingForm(initial={'rating': user_rating.rating})
        except UserRating.DoesNotExist:
            form = MovieRatingForm()

    context = {
        'movie': movie,
        'similar_movies': similar_movies,
        'form': form,
    }

    return render(request, 'movies/netflix-movie-detail.html', context)

@login_required
def watch_movie(request, movie_id):
    """View to redirect to the streaming platform for watching the movie"""
    movie = get_object_or_404(Movie, id=movie_id)

    # Define streaming platform URLs
    streaming_urls = {
        'Netflix': 'https://www.netflix.com/search?q=',
        'Amazon Prime': 'https://www.amazon.com/s?k=',
        'Disney+': 'https://www.disneyplus.com/search?q=',
        'HBO Max': 'https://www.hbomax.com/search?q=',
        'Hulu': 'https://www.hulu.com/search?q=',
        'Paramount+': 'https://www.paramountplus.com/search/?q='
    }

    # Get the base URL for the streaming platform
    platform = movie.streaming_platform
    base_url = streaming_urls.get(platform, 'https://www.google.com/search?q=watch+')

    # Create the search URL with the movie title
    search_query = f"{movie.title} {movie.year}"
    search_url = f"{base_url}{search_query.replace(' ', '+')}"

    # Log the watch activity
    messages.success(request, f"Redirecting to watch '{movie.title}' on {platform}")

    # Redirect to the streaming platform
    return HttpResponseRedirect(search_url)
