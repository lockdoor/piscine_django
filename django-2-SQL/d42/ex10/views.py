from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.utils import ProgrammingError
from .models import Planets, People, Movies
from .forms import Mainform
import sys
from django.db.models import Q

# Create your views here.
def index(request):
	try:
		if Planets.objects.count() == 0:
			return HttpResponse("No data available, please use the following command line before use:<br>python3 manage.py loaddata ../d05/ex10_initial_data.json")
		if request.method == 'POST':
			form = Mainform(request.POST)
			if form.is_valid():
				min_release = form.cleaned_data['min_date']
				max_release = form.cleaned_data['max_date']
				gender = form.cleaned_data['gender']
				diameter = form.cleaned_data['planet_diameter']
				movies = Movies.objects.filter(release_date__gte=min_release, release_date__lte=max_release)
				data = []
				if diameter == 0:
					filters = Q(gender=gender)
				else:
					filters = Q(gender=gender, homeworld__diameter__gte=diameter)
				for movie in movies:
					people = movie.characters.filter(filters).select_related('homeworld')\
						.values('name', 'gender', 'homeworld__name', 'homeworld__diameter')
					for person in people:
						data.append({
							'title': movie.title,
							'name': person['name'],
							'gender': person['gender'],
							'homeworld': person['homeworld__name'],
							'diameter': person['homeworld__diameter']
						})
				# print(data, file=sys.stderr)
				return render(request, 'ex10/index.html', {'form': form, 'data': data})
			else:
				# form = Mainform()
				return render(request, 'ex10/index.html', {'form': form})
		else:
			form = Mainform()
			return render(request, 'ex10/index.html', {'form': form})
	except ProgrammingError as e:
		if e.__str__().startswith('relation "ex10_planets" does not exist'):
			return HttpResponse('relation "ex10_planets" does not exist<br>Usage:<br>python3 manage.py makemigrations ex10<br>python3 manage.py migrate ex10')
		else:
			return HttpResponseBadRequest(f'Error: {e}')
