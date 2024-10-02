from django import forms
from django.db import connection

class MovieRemoveForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(MovieRemoveForm, self).__init__(*args, **kwargs)
		
		# Raw SQL query to get all movie titles
		with connection.cursor() as cursor:
			cursor.execute("SELECT episode_nb, title FROM ex06_movies ORDER BY episode_nb")
			movies = cursor.fetchall()  # Fetch all rows
		
		# Populate the dropdown choices (id, title)
		self.fields['movie'].choices = [(movie[0], movie[1]) for movie in movies]

	# Dropdown field to select movie title
	movie = forms.ChoiceField(choices=[])

class MovieUpdateForm(MovieRemoveForm):
	opening_crawl = forms.CharField(
		widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
		label="Opening Crawl",
		required=True,
	)
