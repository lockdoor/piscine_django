from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest, HttpResponseNotAllowed, HttpResponseForbidden
from .forms import CreateTip, SignUpForm, SignInForm
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
import sys
from .models import Tip
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission

# User = get_user_model()

# Create your views here.
def home(request: HttpRequest):
	tips = Tip.objects.select_related('author')\
		.prefetch_related('upvote', 'downvote')\
		.annotate(
			upvote_count=Count('upvote', distinct=True), 
			downvote_count=Count('downvote', distinct=True))\
		.all()

	if request.user.is_authenticated:
		username = request.user
		form = CreateTip()
	else:
		username = request.session.get('username')
		form = None
	
	context = {
		'username': username,
		'user': request.user,
		'form': form,
		'tips': tips,
	}
	return render(request, 'tip/home.html', context)

@require_POST
@login_required
def create_tip(request):
	form = CreateTip(request.POST)
	if form.is_valid():
		# Create a new Tip object but don't save it to the database yet
		tip = form.save(commit=False)
		# Assign the logged-in user as the author of the tip
		tip.author = request.user
		# Save the tip (this will also auto-set the date due to auto_now_add=True)
		tip.save()
		return redirect('/')

def signup(request: HttpRequest):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	context = {
		'username': request.session.get('username'),
		'form': form,
		'title': 'SignUp'
	}
	return render(request, 'tip/sign.html', context)

def signin(request: HttpRequest):
	if request.method == 'POST':
		form = SignInForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/')
	else:
		form = SignInForm()
	context = {
		'username': request.session.get('username'),
		'form': form,
		'title': 'SignIn'
	}
	return render(request, 'tip/sign.html', context)

def signout(request: HttpRequest):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')

@require_POST
@login_required
def vote(request: HttpRequest):
	tip_id = request.POST.get('tip_id')
	vote_type = request.POST.get('vote_type')
	tip = get_object_or_404(Tip, id=tip_id)

	if vote_type == 'upvote':
		tip.set_upvote(request)
	elif vote_type == 'downvote':
		if not tip.set_downvote(request):
			return HttpResponseForbidden('You not have permission!!')
	else:
		return HttpResponseBadRequest("vote type error!!")
	tip.save()
	return redirect('/')

@require_POST
@login_required
# @permission_required('tip.can_delete_tip', raise_exception=True)
def remove(request: HttpRequest):
	tip_id = request.POST.get('tip_id')
	tip = get_object_or_404(Tip, id=tip_id)
	# if tip.author == request.user or request.user.groups.filter(name='tip_delete').exists():
	if tip.author == request.user or request.user.has_perm('tip.delete_tip'):
		tip.delete()
		return redirect('/')
	else:
		return HttpResponseForbidden('You not have permission!!')
