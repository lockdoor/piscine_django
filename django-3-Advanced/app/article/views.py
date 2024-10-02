# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article

# Create your views here.
class ArticlesView(ListView):
    model = Article
    template_name = 'base.html'