from django.contrib import admin
from .models import Genre, Language, Movie, Mood, MoodGenreMapping, UserPreference, UserRating

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'length_category', 'period_category', 'imdb_rating')
    list_filter = ('length_category', 'period_category', 'genres', 'languages')
    search_fields = ('title', 'description')
    filter_horizontal = ('genres', 'languages')

@admin.register(MoodGenreMapping)
class MoodGenreMappingAdmin(admin.ModelAdmin):
    list_display = ('mood', 'genre', 'weight')
    list_filter = ('mood', 'genre')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_length', 'preferred_period')
    list_filter = ('preferred_length', 'preferred_period', 'preferred_genres', 'preferred_languages')
    filter_horizontal = ('preferred_genres', 'preferred_languages')

@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating')
    list_filter = ('rating',)
    search_fields = ('user__username', 'movie__title')
