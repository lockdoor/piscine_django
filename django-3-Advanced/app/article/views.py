from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article
from django.conf import settings
import sys

# Create your views here.
class ArticlesListView(ListView):
    model = Article
    template_name = 'article/articles.html'

class PublicationsListView(ListView):
    model = Article
    template_name = 'article/publications.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

class FavouritesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article/favourites.html'

class RegisterCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.LOGIN_URL

class PublishCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'synopsis', 'content']
    template_name = 'article/publish.html'
    success_url = '/publications'

    # Override the form_valid method to assign the author
    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the current user as the author
        return super().form_valid(form)



'''
for infomation of DetailView and ListView
https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/
'''

'''
for infomation of CreateView
https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/
'''