from django.shortcuts import render, redirect
from django.http import HttpResponse
from ex01.models import Movies
from .forms import MovieRemoveForm
import sys

# Create your views here.
def populate(request):
	try:
		Movies.objects.create(title='The Phantom Menace', director='Geoge Lucus', producer='Rick McCallum', release_date='1999-05-19')
		Movies.objects.create(title='Attack of the Clones', director='Geoge Lucus', producer='Rick McCallum', release_date='2002-05-16')
		Movies.objects.create(title='Revenge of the Sith', director='Geoge Lucus', producer='Rick McCallum', release_date='2005-05-19')
		Movies.objects.create(title='A New Hope', director='Geoge Lucus', producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25')
		Movies.objects.create(title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17')
		Movies.objects.create(title='Return of the Jedi', director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25')
		Movies.objects.create(title='The Force Awakens', director='J. J. Abrams', producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11')
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(e)

def display(request):
	try:
		movies=Movies.objects.all()
		return render(request, 'ex05/display.html',{'movies': movies})

	except Exception as e:
		return HttpResponse(f'Error: {e}')

def remove(request):
	if request.method == 'POST':
		form = MovieRemoveForm(request.POST)
		if form.is_valid():
			movie = form.cleaned_data['movie']
			movie.delete()
			return redirect('../display/')
		else:
			return HttpResponse('Form invalid\n')
	else:
		form = MovieRemoveForm()
		return render(request, 'ex04/remove.html', {'form': form})
