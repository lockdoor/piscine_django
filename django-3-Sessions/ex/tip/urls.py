from django.urls import path
from . import views

urlpatterns = [
	path("", views.home),
	path("home", views.home),
	path("signup", views.signup),
	path("signin", views.signin),
	path("signout", views.signout),
	path("vote", views.vote, name='vote'),
	path("remove", views.remove, name='remove'),
	path("create_tip", views.create_tip, name='create_tip'),
]
