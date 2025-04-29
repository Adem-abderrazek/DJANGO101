from django import forms
from .models import Genre, Language, Mood, Movie, UserPreference

class MoviePreferenceForm(forms.Form):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select your preferred genres"
    )
    
    mood = forms.ModelChoiceField(
        queryset=Mood.objects.all(),
        required=False,
        empty_label="Select your mood",
        label="How are you feeling today?"
    )
    
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select preferred languages"
    )
    
    length = forms.ChoiceField(
        choices=[('', 'Any')] + list(Movie.LENGTH_CHOICES),
        required=False,
        label="Movie length"
    )
    
    period = forms.ChoiceField(
        choices=[('', 'Any')] + list(Movie.PERIOD_CHOICES),
        required=False,
        label="Release period"
    )
    
    def save_preferences(self, user):
        """Save user preferences to the database"""
        user_pref, created = UserPreference.objects.get_or_create(user=user)
        
        # Clear existing preferences
        user_pref.preferred_genres.clear()
        user_pref.preferred_languages.clear()
        
        # Add new preferences
        if self.cleaned_data.get('genres'):
            user_pref.preferred_genres.add(*self.cleaned_data['genres'])
        
        if self.cleaned_data.get('languages'):
            user_pref.preferred_languages.add(*self.cleaned_data['languages'])
        
        if self.cleaned_data.get('length'):
            user_pref.preferred_length = self.cleaned_data['length']
        else:
            user_pref.preferred_length = None
            
        if self.cleaned_data.get('period'):
            user_pref.preferred_period = self.cleaned_data['period']
        else:
            user_pref.preferred_period = None
            
        user_pref.save()
        return user_pref

class MovieRatingForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'}),
        label="Your Rating (1-5)"
    )
