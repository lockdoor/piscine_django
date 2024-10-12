from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
import os, sys
# Create your views here.
def connect():
	return psycopg2.connect(
		f'''
		dbname={os.getenv('dbname')}
		user={os.getenv('user')}
		password={os.getenv('password')}
		host={os.getenv('host')}
		port={os.getenv('port')}
		'''	
	)

create_table_planets_sql_text = '''
	CREATE TABLE ex08_planets (
		id SERIAL PRIMARY KEY,
		name VARCHAR(64) UNIQUE NOT NULL,
		climate VARCHAR,
		diameter INT DEFAULT 0,
		orbital_period INT DEFAULT 0,
		population BIGINT DEFAULT 0,
		robital_period INT DEFAULT 0,
		surface_water REAL DEFAULT 0,
		terrain VARCHAR(128)
	);
	'''

create_table_people_sql_text = '''
	CREATE TABLE ex08_people (
		id SERIAL PRIMARY KEY,
		name VARCHAR(64) UNIQUE NOT NULL,
		birth_year VARCHAR(32),
		gender VARCHAR(32),
		eye_color VARCHAR(32),
		hair_color VARCHAR(32),
		height INT,
		mass REAL,
		homeworld VARCHAR(64),
		CONSTRAINT fk_homeworld 
			FOREIGN KEY(homeworld) 
				REFERENCES ex08_planets(name)
				ON DELETE SET NULL
	)
'''

planets_columns: tuple = ('name', 'climate', 'diameter', 'orbital_period', 
	'population', 'robital_period', 'surface_water', 'terrain')

people_columns: tuple = ('name', 'birth_year', 'gender', 'eye_color',
	'hair_color', 'height', 'mass', 'homeworld')

def init(request):
	try:
		conn = connect()
		try:
			curs = conn.cursor()
			curs.execute(create_table_planets_sql_text)
			curs.execute(create_table_people_sql_text)
			conn.commit()
			curs.close()
			return HttpResponse('OK')
		except Exception as e:
			conn.rollback()
			return HttpResponse(f'Error: {e}')
		finally:
			conn.close()
	except Exception as e:
		return HttpResponse(f'Error: {e}')

def populate(request):
	try:
		conn = connect()
		try:
			curs = conn.cursor()
			file = open("d05/planets.csv", 'r')
			curs.copy_from(file=file, table='ex08_planets', columns=planets_columns, null='NULL')
			file.close()
			file = open("d05/people.csv", 'r')
			curs.copy_from(file=file, table='ex08_people', columns=people_columns, null='NULL')
			file.close()
			curs.close()
			conn.commit()
			return HttpResponse('OK')
		except Exception as e:
			return HttpResponse(f'Error: {e}')
		finally:
			conn.close()
	except Exception as e:
		return HttpResponse(f'Error: {e}')

def display(request):
	try:
		with connect() as conn:
			curs = conn.cursor()
			curs.execute('''
				SELECT people.id, people.name, planets.climate, people.homeworld 
				FROM ex08_people as people 
				LEFT JOIN ex08_planets as planets ON people.homeworld=planets.name 
				WHERE climate LIKE '%windy%' 
				ORDER BY people.name;
			''')
			people = curs.fetchall()
			return render(request, 'ex08/display.html', {'people': people})
	except Exception as e:
		return HttpResponse(f'Error: {e}')
