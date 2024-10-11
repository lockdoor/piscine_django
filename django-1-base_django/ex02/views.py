from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseBadRequest
from .forms import sample_form
from django.conf import settings
import time
# import sys

# Create your views here.
def my_form(request):
	if request.method == 'POST':
		form = sample_form(request.POST)
		if form.is_valid():
			history = form.cleaned_data['text']
			with open(settings.LOGS, 'a') as fs:
				fs.write(f"{history} : {time.time()}\n")
			form = sample_form
	else:
		form = sample_form
	try:
		histories = []
		with open(settings.LOGS, 'r') as fs:	
			for line in fs:
				histories.append(line)
	except FileNotFoundError:
		pass
	return render(request, "ex02/index.html", {'form': form, 'histories': histories})
	
	

'''
def my_form(request):
	if request.method == 'POST':
		form = forms.sample_form(request.POST)
		if form.is_valid():
			file = open(settings.LOGS, 'a')
			print(f"{request.POST['text']} : {time.time()}", file=file)
			file.close()
			return history(request)
		else:
			return HttpResponseBadRequest("form invalid")
	else:
		form = forms.sample_form()
		return render(request, 'ex02/index.html', {"form": form})

def history(request):
	history: list = []
	try:
		file = open(settings.LOGS, "r")
		for f in file:
			history.append(f)
		file.close()
	except FileNotFoundError:
		pass
	return render(request, 'ex02/history.html', {"history": history})
'''
