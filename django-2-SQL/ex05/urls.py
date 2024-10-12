from django.urls import path
from . import views

app_name = "ex05"

urlpatterns = [
    path('populate/', views.populate),
    path('display/', views.display),
    path('remove/', views.remove, name="remove"),
]