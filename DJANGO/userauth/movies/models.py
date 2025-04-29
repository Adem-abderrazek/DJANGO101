from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    LENGTH_CHOICES = [
        ('short', 'Short (<90 min)'),
        ('normal', 'Normal (90-120 min)'),
        ('long', 'Long (>120 min)'),
    ]

    PERIOD_CHOICES = [
        ('recent', 'Recent (last 5 years)'),
        ('modern', 'Modern (last 20 years)'),
        ('classic', 'Classic (older than 20 years)'),
    ]

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    length_category = models.CharField(max_length=10, choices=LENGTH_CHOICES)
    period_category = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    duration_minutes = models.IntegerField()
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    imdb_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    streaming_platform = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Mood(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class MoodGenreMapping(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    weight = models.FloatField(default=1.0)

    class Meta:
        unique_together = ('mood', 'genre')

    def __str__(self):
        return f"{self.mood.name} - {self.genre.name} ({self.weight})"

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_genres = models.ManyToManyField(Genre, blank=True)
    preferred_languages = models.ManyToManyField(Language, blank=True)
    preferred_length = models.CharField(max_length=10, choices=Movie.LENGTH_CHOICES, blank=True, null=True)
    preferred_period = models.CharField(max_length=10, choices=Movie.PERIOD_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title}: {self.rating}"
