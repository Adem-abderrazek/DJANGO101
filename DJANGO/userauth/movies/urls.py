from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.preference_form, name='movie_preferences'),
    path('recommendations/', views.movie_recommendations, name='movie_recommendations'),
    path('recommendations/<int:mood_id>/', views.movie_recommendations, name='movie_recommendations'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('watch/<int:movie_id>/', views.watch_movie, name='watch_movie'),
]
