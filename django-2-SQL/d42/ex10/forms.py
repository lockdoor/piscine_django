from django import forms
from .models import Movies, People
from django.db.models import Min, Max

class Mainform(forms.Form):
	min_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	max_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	planet_diameter = forms.IntegerField(min_value=0, initial=0)
	gender = forms.ChoiceField(choices=[])

	def __init__(self, *args, **kwargs):
		super(Mainform, self).__init__(*args, **kwargs)
		
		# Get min and max release date from the database
		min_date = Movies.objects.aggregate(Min('release_date'))['release_date__min']
		max_date = Movies.objects.aggregate(Max('release_date'))['release_date__max']
		
		# Set the min and max attributes for the date input
		min = min_date.strftime('%Y-%m-%d') if min_date else None
		max = max_date.strftime('%Y-%m-%d') if max_date else None
		self.fields['min_date'].widget.attrs['min'] = min
		self.fields['min_date'].widget.attrs['max'] = max
		self.fields['min_date'].widget.attrs['value'] = min
		self.fields['max_date'].widget.attrs['min'] = min
		self.fields['max_date'].widget.attrs['max'] = max
		self.fields['max_date'].widget.attrs['value'] = max

		distinct_gender = People.objects.values_list('gender', flat=True).distinct()
		gender_choices = [(gender, gender) for gender in distinct_gender]
		self.fields['gender'].choices = gender_choices
