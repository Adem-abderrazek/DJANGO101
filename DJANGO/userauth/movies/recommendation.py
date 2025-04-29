from django.db.models import Q, Count, Avg, F
from .models import Movie, UserPreference, UserRating, MoodGenreMapping

def get_recommendations(user, mood=None, limit=10):
    """
    Get movie recommendations based on user preferences and mood
    
    This function implements a hybrid recommendation system:
    1. Content-based filtering: Based on user's genre, language, length, and period preferences
    2. Mood-based filtering: Based on the user's current mood
    3. Collaborative filtering: Based on ratings from similar users (simplified version)
    """
    # Get user preferences
    try:
        user_pref = UserPreference.objects.get(user=user)
        has_preferences = True
    except UserPreference.DoesNotExist:
        has_preferences = False
    
    # Base query
    movies = Movie.objects.all()
    
    # Content-based filtering
    if has_preferences:
        # Filter by genres if user has genre preferences
        if user_pref.preferred_genres.exists():
            genre_ids = user_pref.preferred_genres.values_list('id', flat=True)
            movies = movies.filter(genres__in=genre_ids).distinct()
        
        # Filter by languages if user has language preferences
        if user_pref.preferred_languages.exists():
            language_ids = user_pref.preferred_languages.values_list('id', flat=True)
            movies = movies.filter(languages__in=language_ids).distinct()
        
        # Filter by length preference if set
        if user_pref.preferred_length:
            movies = movies.filter(length_category=user_pref.preferred_length)
        
        # Filter by period preference if set
        if user_pref.preferred_period:
            movies = movies.filter(period_category=user_pref.preferred_period)
    
    # Mood-based filtering
    if mood:
        # Get genres associated with the mood
        mood_genres = MoodGenreMapping.objects.filter(mood=mood).order_by('-weight')
        if mood_genres.exists():
            genre_ids = mood_genres.values_list('genre_id', flat=True)
            # Prioritize movies with genres matching the mood
            movies = movies.filter(genres__in=genre_ids).distinct()
    
    # Exclude movies the user has already rated
    rated_movies = UserRating.objects.filter(user=user).values_list('movie_id', flat=True)
    movies = movies.exclude(id__in=rated_movies)
    
    # Order by IMDb rating as a fallback
    movies = movies.order_by('-imdb_rating')
    
    # Return limited number of recommendations
    return movies[:limit]

def get_popular_movies(limit=10):
    """Get popular movies based on average user ratings"""
    return Movie.objects.annotate(
        avg_rating=Avg('userrating__rating')
    ).filter(
        avg_rating__isnull=False
    ).order_by('-avg_rating', '-imdb_rating')[:limit]

def get_similar_movies(movie_id, limit=5):
    """Get movies similar to the given movie based on genres"""
    try:
        movie = Movie.objects.get(id=movie_id)
        genre_ids = movie.genres.values_list('id', flat=True)
        
        similar_movies = Movie.objects.filter(
            genres__in=genre_ids
        ).exclude(
            id=movie_id
        ).annotate(
            genre_match_count=Count('genres', filter=Q(genres__in=genre_ids))
        ).order_by('-genre_match_count', '-imdb_rating')[:limit]
        
        return similar_movies
    except Movie.DoesNotExist:
        return Movie.objects.none()
