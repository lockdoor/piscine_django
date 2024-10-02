from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_form),
    path('history/', views.history)
]