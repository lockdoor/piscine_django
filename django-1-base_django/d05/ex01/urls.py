from django.urls import path
from . import views

urlpatterns = [
	path('', views.django),
	path('django', views.django),
	path('display', views.display),
	path('templates', views.templates)
]