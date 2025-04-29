from django.core.management.base import BaseCommand
from movies.models import Genre, Language, Movie

class Command(BaseCommand):
    help = 'Adds even more sample movies to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding even more movies...')
        
        # Sample movies data
        movies_data = [
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'year': 2001,
                'description': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.',
                'genres': ['Adventure', 'Drama', 'Fantasy'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 178,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_.jpg',
                'imdb_rating': 8.8,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Fight Club',
                'year': 1999,
                'description': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.',
                'genres': ['Drama'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 139,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YzVmLWI0ZTEtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'imdb_rating': 8.8,
                'streaming_platform': 'Hulu'
            },
            {
                'title': 'Goodfellas',
                'year': 1990,
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.',
                'genres': ['Biography', 'Crime', 'Drama'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 146,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'imdb_rating': 8.7,
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
                'title': 'The Avengers',
                'year': 2012,
                'description': 'Earth\'s mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.',
                'genres': ['Action', 'Adventure', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 143,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'imdb_rating': 8.0,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'The Shining',
                'year': 1980,
                'description': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.',
                'genres': ['Drama', 'Horror'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 146,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Jurassic Park',
                'year': 1993,
                'description': 'A pragmatic paleontologist visiting an almost complete theme park is tasked with protecting a couple of kids after a power failure causes the park\'s cloned dinosaurs to run loose.',
                'genres': ['Action', 'Adventure', 'Science Fiction'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 127,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg',
                'imdb_rating': 8.1,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Truman Show',
                'year': 1998,
                'description': 'An insurance salesman discovers his whole life is actually a reality TV show.',
                'genres': ['Comedy', 'Drama'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 103,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMDIzODcyY2EtMmY2MC00ZWVlLTgwMzAtMjQwOWUyNmJjNTYyXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_.jpg',
                'imdb_rating': 8.1,
                'streaming_platform': 'Amazon Prime'
            },
            {
                'title': 'Titanic',
                'year': 1997,
                'description': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
                'genres': ['Drama', 'Romance'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 194,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg',
                'imdb_rating': 7.9,
                'streaming_platform': 'Paramount+'
            },
            {
                'title': 'The Sixth Sense',
                'year': 1999,
                'description': 'A boy who communicates with spirits seeks the help of a disheartened child psychologist.',
                'genres': ['Drama', 'Mystery', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'classic',
                'duration_minutes': 107,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMWM4NTFhYjctNzUyNi00NGMwLTk3NTYtMDIyNTZmMzRlYmQyXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_.jpg',
                'imdb_rating': 8.1,
                'streaming_platform': 'Disney+'
            },
            {
                'title': 'Gladiator',
                'year': 2000,
                'description': 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.',
                'genres': ['Action', 'Adventure', 'Drama'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 155,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Green Mile',
                'year': 1999,
                'description': 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.',
                'genres': ['Crime', 'Drama', 'Fantasy'],
                'languages': ['English'],
                'length_category': 'long',
                'period_category': 'classic',
                'duration_minutes': 189,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg',
                'imdb_rating': 8.6,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Inglourious Basterds',
                'year': 2009,
                'description': 'In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner\'s vengeful plans for the same.',
                'genres': ['Adventure', 'Drama', 'War'],
                'languages': ['English', 'German', 'French'],
                'length_category': 'long',
                'period_category': 'modern',
                'duration_minutes': 153,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg',
                'imdb_rating': 8.3,
                'streaming_platform': 'Netflix'
            },
            {
                'title': 'The Prestige',
                'year': 2006,
                'description': 'After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.',
                'genres': ['Drama', 'Mystery', 'Science Fiction', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 130,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg',
                'imdb_rating': 8.5,
                'streaming_platform': 'HBO Max'
            },
            {
                'title': 'Memento',
                'year': 2000,
                'description': 'A man with short-term memory loss attempts to track down his wife\'s murderer.',
                'genres': ['Mystery', 'Thriller'],
                'languages': ['English'],
                'length_category': 'normal',
                'period_category': 'modern',
                'duration_minutes': 113,
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg',
                'imdb_rating': 8.4,
                'streaming_platform': 'Amazon Prime'
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
