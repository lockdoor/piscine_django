from django import forms
from .models import Movies

# class movie_form(forms.ModelForm):
# 	class Meta:
# 		model = Movies
# 		fields = ['title', 'director', 'producer', 'release_date']

class MovieRemoveForm(forms.Form):
    movie = forms.ModelChoiceField(
        queryset=Movies.objects.all(),  # Query all movies
        label="Select Movie Title",  # Label for the dropdown
        # empty_label="Choose a Movie"  # Default label in the dropdown
				empty_label=None
    )
