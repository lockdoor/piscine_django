from django.urls import path
from . import views

app_name = "ex04"

urlpatterns = [
    path('init/', views.init),
    path('populate/', views.populate),
    path('display/', views.display),
    path('remove/', views.remove, name="remove")
]