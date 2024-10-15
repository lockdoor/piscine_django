from django.urls import path
from . import views

app_name = 'tip'

urlpatterns = [
	path("", views.home, name="home"),
	path("home", views.home, name="home"),
	path("signup", views.signup, name="signup"),
	path("signin", views.signin, name="signin"),
	path("signout", views.signout, name="signout"),
	path("vote", views.vote, name='vote'),
	path("remove", views.remove, name='remove'),
	path("create_tip", views.create_tip, name='create_tip'),
]
