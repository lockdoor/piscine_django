from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Planets, People
from django.db.utils import ProgrammingError
import sys

# Create your views here.
def display(request):
	try:
		if Planets.objects.count() == 0:
			return HttpResponse("No data available, please use the following command line before use:<br>python3 manage.py loaddata ../d05/ex09_initial_data.json")
		
		planets = Planets.objects.filter(climate__contains='windy').prefetch_related('planet')
		# Get all related people for all planets
		people: list[People]= [person for planet in planets for person in planet.planet.all()]

		data: list = []
		for person in people:
			data.append ({
				'name': person.name,
				'id': person.id,
				'homeworld': person.homeworld.name,
				'climate': person.homeworld.climate,
			})
			print(data, file=sys.stderr)


		return render(request, 'ex09/display.html', {'people': data})
		# return HttpResponse('OK')
	except ProgrammingError as e:
		if e.__str__().startswith('relation "ex09_planets" does not exist'):
			return HttpResponse('relation "ex09_planets" does not exist<br>Usage:<br>python3 manage.py makemigrations ex09<br>python3 manage.py migrate ex09')
		else:
			return HttpResponseBadRequest(f'Error: {e}')
