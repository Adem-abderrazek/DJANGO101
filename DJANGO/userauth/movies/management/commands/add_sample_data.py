from django.core.management.base import BaseCommand
from movies.models import Genre, Language, Mood, Movie, MoodGenreMapping
import random

class Command(BaseCommand):
    help = 'Adds sample data to the movie recommender app'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding sample data...')
        
        # Add genres
        genres = [
            'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary',
            'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery',
            'Romance', 'Science Fiction', 'Thriller', 'War', 'Western'
        ]
        
        for genre_name in genres:
            Genre.objects.get_or_create(name=genre_name)
        
        self.stdout.write(self.style.SUCCESS(f'Added {len(genres)} genres'))
        
        # Add languages
        languages = [
            'English', 'Spanish', 'French', 'German', 'Italian', 'Japanese',
            'Korean', 'Chinese', 'Hindi', 'Arabic', 'Russian', 'Portuguese'
        ]
        
        for language_name in languages:
            Language.objects.get_or_create(name=language_name)
        
        self.stdout.write(self.style.SUCCESS(f'Added {len(languages)} languages'))
        
        # Add moods
        moods = [
            'Happy', 'Sad', 'Excited', 'Relaxed', 'Romantic', 'Thoughtful',
            'Nostalgic', 'Inspired', 'Tense', 'Curious'
        ]
        
        for mood_name in moods:
            Mood.objects.get_or_create(name=mood_name)
        
        self.stdout.write(self.style.SUCCESS(f'Added {len(moods)} moods'))
        
        # Add mood-genre mappings
        self.create_mood_genre_mappings()
        
        # Add sample movies
        self.add_sample_movies()
        
        self.stdout.write(self.style.SUCCESS('Sample data added successfully!'))
    
    def create_mood_genre_mappings(self):
        # Get all moods and genres
        moods = Mood.objects.all()
        genres = Genre.objects.all()
        
        # Define mood-genre relationships with weights
        mood_mappings = {
            'Happy': ['Comedy', 'Animation', 'Family', 'Music'],
            'Sad': ['Drama', 'Romance', 'War'],
            'Excited': ['Action', 'Adventure', 'Science Fiction', 'Thriller'],
            'Relaxed': ['Documentary', 'Animation', 'Family'],
            'Romantic': ['Romance', 'Drama', 'Comedy'],
            'Thoughtful': ['Drama', 'Mystery', 'History', 'Documentary'],
            'Nostalgic': ['History', 'Family', 'Music'],
            'Inspired': ['Documentary', 'Drama', 'Biography', 'Music'],
            'Tense': ['Thriller', 'Horror', 'Crime', 'Mystery'],
            'Curious': ['Mystery', 'Science Fiction', 'Documentary', 'Fantasy']
        }
        
        # Create mappings
        mappings_created = 0
        for mood in moods:
            if mood.name in mood_mappings:
                related_genres = mood_mappings[mood.name]
                for genre_name in related_genres:
                    try:
                        genre = Genre.objects.get(name=genre_name)
                        weight = 1.0
                        MoodGenreMapping.objects.get_or_create(
                            mood=mood,
                            genre=genre,
                            defaults={'weight': weight}
                        )
                        mappings_created += 1
                    except Genre.DoesNotExist:
                        continue
        
        self.stdout.write(self.style.SUCCESS(f'Created {mappings_created} mood-genre mappings'))
    
    def add_sample_movies(self):
        # Sample movies data
        movies_data = [
            {
                'title': 'The Shawshank Redemption',
                'year': 1994,
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'genres': ['Drama'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 142,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg',
                'imdb_rating': 9.3,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Godfather',
                'year': 1972,
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'genres': ['Crime', 'Drama'],
                'languages': ['English', 'Italian'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 175,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'imdb_rating': 9.2,
                'streaming_platform': 'Amazon Prime'
            },
            {
                'title': 'Inception',
                'year': 2010,
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'genres': ['Action', 'Adventure', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 148,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg',
                'imdb_rating': 8.8,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Parasite',
                'year': 2019,
                'description': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
                'genres': ['Comedy', 'Drama', 'Thriller'],
                'languages': ['Korean'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 132,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'Hulu'
            },
            {
                'title': 'The Lion King',
                'year': 1994,
                'description': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.',
                'genres': ['Animation', 'Adventure', 'Drama'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 88,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'Toy Story',
                'year': 1995,
                'description': 'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\'s room.',
                'genres': ['Animation', 'Adventure', 'Comedy'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 81,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_.jpg',
                'imdb_rating': 8.3,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'The Dark Knight',
                'year': 2008,
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'genres': ['Action', 'Crime', 'Drama'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 152,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg',
                'imdb_rating': 9.0,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'Spirited Away',
                'year': 2001,
                'description': 'During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.',
                'genres': ['Animation', 'Adventure', 'Family'],
                'languages': ['Japanese'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 125,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMjlmZmI5MDctNDE2YS00YWE0LWE5ZWItZDBhYWQ0NTcxNWRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'imdb_rating': 8.6,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Coco',
                'year': 2017,
                'description': 'Aspiring musician Miguel, confronted with his family\'s ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.',
                'genres': ['Animation', 'Adventure', 'Family'],
                'languages': ['English', 'Spanish'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 105,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'Get Out',
                'year': 2017,
                'description': 'A young African-American visits his white girlfriend\'s parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.',
                'genres': ['Horror', 'Mystery', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 104,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_.jpg',
                'imdb_rating': 7.7,
                'streaming_platform': 'Netflix'
            }
        ]
        
        # Add movies
        movies_added = 0
        for movie_data in movies_data:
            # Extract genres and languages
            genre_names = movie_data.pop('genres')
            language_names = movie_data.pop('languages')
            
            # Create movie
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                year=movie_data['year'],
                defaults=movie_data
            )
            
            if created:
                movies_added += 1
            
            # Add genres
            for genre_name in genre_names:
                try:
                    genre = Genre.objects.get(name=genre_name)
                    movie.genres.add(genre)
                except Genre.DoesNotExist:
                    continue
            
            # Add languages
            for language_name in language_names:
                try:
                    language = Language.objects.get(name=language_name)
                    movie.languages.add(language)
                except Language.DoesNotExist:
                    continue
        
        self.stdout.write(self.style.SUCCESS(f'Added {movies_added} sample movies'))
