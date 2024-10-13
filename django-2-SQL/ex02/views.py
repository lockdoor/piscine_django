from django.shortcuts import render
from django.http import HttpResponse
# from ex00.views import init as ex00_init
import psycopg2 
from psycopg2 import extensions
import os, sys

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

def create_table(conn: extensions.connection, table_name: str):
	cursor = conn.cursor()
	cursor.execute(
	f'''
	CREATE TABLE {table_name} (
		title VARCHAR(64) NOT NULL UNIQUE,
		episode_nb BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
		opening_crawl TEXT,
		director VARCHAR(32) NOT NULL,
		producer VARCHAR(128) NOT NULL,
		release_date DATE NOT NULL
	);
	''')
	conn.commit()

# def insert_into(conn: extensions.connection, sql: str):
# 	cursor = conn.cursor()
# 	cursor.execute(sql)
# 	conn.commit()

# Create your views here.
def init(request):
	try:
		conn = connect()
		try:
			create_table(conn, 'ex02_movies')
			return HttpResponse('OK\n')
		except psycopg2.Error as e:
			conn.rollback()
			return HttpResponse(f'Error: {e}')
		finally:
			conn.close()
		
	except psycopg2.OperationalError:
		return HttpResponse("Error: can not connect database")

'''
It must return a page displaying "OK" for each successful insertion. Otherwise, it
must display an error message stating the problem.
'''
def populate(request):
	try:
		conn = connect()
		feedback:str = ""
		try:
			datas: list[tuple] = [
				('The Phantom Menace', 'Geoge Lucus', 'Rick McCallum', '1999-05-19'),
				('Attack of the Clones', 'Geoge Lucus', 'Rick McCallum', '2002-05-16'),
				('Revenge of the Sith', 'Geoge Lucus', 'Rick McCallum', '2005-05-19'),
				('A New Hope', 'Geoge Lucus', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
				('The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
				('Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
				('The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
			]
			cursor = conn.cursor()
			for data in datas:
				try:
					cursor.execute("INSERT INTO ex04_movies (title, director, producer, release_date) VALUES (%s, %s, %s, %s)", data)
					feedback += f'INSERT {data[0]} OK<br>'
					conn.commit()
				except psycopg2.Error as e:
					conn.rollback()
					feedback += f'{str(e)}<br>'
		except Exception as e:
			feedback = str(e)
		finally:
			conn.close()
			return HttpResponse(feedback)

	except psycopg2.OperationalError:
		return HttpResponse("Error: can not connect database")

def display(request):
	try:
		conn = connect()
		try:
			cur = conn.cursor()
			cur.execute("SELECT title, director, producer, release_date FROM ex02_movies;")
			movies = cur.fetchall()
			return render(request, 'ex02/display.html', {"movies": movies})
		except psycopg2.Error as e:
			conn.rollback()
			return HttpResponse(f'Error: {e}')
		finally:
			conn.close()

	except psycopg2.OperationalError:
		return HttpResponse("Error: can not connect database")
