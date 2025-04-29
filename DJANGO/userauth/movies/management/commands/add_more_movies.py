from django.core.management.base import BaseCommand
from movies.models import Genre, Language, Movie

class Command(BaseCommand):
    help = 'Adds more sample movies to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding more movies...')
        
        # Sample movies data
        movies_data = [
            {
                'title': 'The Matrix',
                'year': 1999,
                'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                'genres': ['Action', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 136,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg',
                'imdb_rating': 8.7,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Pulp Fiction',
                'year': 1994,
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                'genres': ['Crime', 'Drama'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 154,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'imdb_rating': 8.9,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'Forrest Gump',
                'year': 1994,
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
                'genres': ['Drama', 'Romance'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 142,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                'imdb_rating': 8.8,
                'streaming_platform': 'Amazon Prime'
            },
            {
                'title': 'Interstellar',
                'year': 2014,
                'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
                'genres': ['Adventure', 'Drama', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 169,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'imdb_rating': 8.6,
                'streaming_platform': 'Paramount+'
            },
            {
                'title': 'The Silence of the Lambs',
                'year': 1991,
                'description': 'A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.',
                'genres': ['Crime', 'Drama', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 118,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg',
                'imdb_rating': 8.6,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'Your Name',
                'year': 2016,
                'description': 'Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?',
                'genres': ['Animation', 'Drama', 'Fantasy', 'Romance'],
                'languages': ['Japanese'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 106,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcxYThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Grand Budapest Hotel',
                'year': 2014,
                'description': 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel\'s glorious years under an exceptional concierge.',
                'genres': ['Adventure', 'Comedy', 'Crime'],
                'languages': ['English', 'French', 'German'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 99,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_.jpg',
                'imdb_rating': 8.1,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'Whiplash',
                'year': 2014,
                'description': 'A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student\'s potential.',
                'genres': ['Drama', 'Music'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 106,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BOTA5NDZlZGUtMjAxOS00YTRkLTkwYmMtYWQ0NWEwZDZiNjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'La La Land',
                'year': 2016,
                'description': 'While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.',
                'genres': ['Comedy', 'Drama', 'Music', 'Romance'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 128,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg',
                'imdb_rating': 8.0,
                'streaming_platform': 'Hulu'
            },
            {
                'title': 'Black Panther',
                'year': 2018,
                'description': 'T\'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country\'s past.',
                'genres': ['Action', 'Adventure', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 134,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_.jpg',
                'imdb_rating': 7.3,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'The Departed',
                'year': 2006,
                'description': 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
                'genres': ['Crime', 'Drama', 'Thriller'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 151,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Amélie',
                'year': 2001,
                'description': 'Amélie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.',
                'genres': ['Comedy', 'Romance'],
                'languages': ['French'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 122,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNDg4NjM1YjMtYmNhZC00MjM0LWFiZmYtNGY1YjA3MzZmODc5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_.jpg',
                'imdb_rating': 8.3,
                'streaming_platform': 'Amazon Prime'
            },
            {
                'title': 'Oldboy',
                'year': 2003,
                'description': 'After being kidnapped and imprisoned for fifteen years, Oh Dae-Su is released, only to find that he must find his captor in five days.',
                'genres': ['Action', 'Drama', 'Mystery', 'Thriller'],
                'languages': ['Korean'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 120,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'Eternal Sunshine of the Spotless Mind',
                'year': 2004,
                'description': 'When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories.',
                'genres': ['Drama', 'Romance', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 108,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_.jpg',
                'imdb_rating': 8.3,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Social Network',
                'year': 2010,
                'description': 'As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.',
                'genres': ['Biography', 'Drama'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 120,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'imdb_rating': 7.7,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'Joker',
                'year': 2019,
                'description': 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.',
                'genres': ['Crime', 'Drama', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'recent',
                'duration_minutes': 122,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'HBO Max'
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
                    # Create genre if it doesn't exist
                    genre = Genre.objects.create(name=genre_name)
                    movie.genres.add(genre)
            
            # Add languages
            for language_name in language_names:
                try:
                    language = Language.objects.get(name=language_name)
                    movie.languages.add(language)
                except Language.DoesNotExist:
                    # Create language if it doesn't exist
                    language = Language.objects.create(name=language_name)
                    movie.languages.add(language)
        
        self.stdout.write(self.style.SUCCESS(f'Added {movies_added} more movies'))
