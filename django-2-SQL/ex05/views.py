from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from .forms import MovieRemoveForm

# Create your views here.

'''
It must return a page displaying "OK" for each successful insertion. Otherwise, it
must display an error message stating the problem.
'''
def populate(request):
	datas: list[dict] = [
		{'title':'The Phantom Menace', 'director':'Geoge Lucus', 'producer':'Rick McCallum', 'release_date':'1999-05-19'},
		{'title':'Attack of the Clones', 'director':'Geoge Lucus', 'producer':'Rick McCallum', 'release_date':'2002-05-16'},
		{'title':'Revenge of the Sith', 'director':'Geoge Lucus', 'producer':'Rick McCallum', 'release_date':'2005-05-19'},
		{'title':'A New Hope', 'director':'Geoge Lucus', 'producer':'Gary Kurtz, Rick McCallum', 'release_date':'1977-05-25'},
		{'title':'The Empire Strikes Back', 'director':'Irvin Kershner', 'producer':'Gary Kurtz, Rick McCallum', 'release_date':'1980-05-17'},
		{'title':'Return of the Jedi', 'director':'Richard Marquand', 'producer':'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date':'1983-05-25'},
		{'title':'The Force Awakens', 'director':'J. J. Abrams', 'producer':'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date':'2015-12-11'},
	]
	feedback = ""
	for data in datas:
		try:
			Movies.objects.create(**data)
			feedback += f'INSERT {data['title']} OK<br>'
		except Exception as e:
			feedback += f'{str(e)}<br>'
	return HttpResponse(feedback)

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
			form = MovieRemoveForm()
	else:
		form = MovieRemoveForm()
	return render(request, 'ex05/remove.html', {'form': form})
