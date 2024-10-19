from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .models import Article, UserFavouriteArticle
from .forms import AddFavouritForm
from django.conf import settings
import sys

# Create your views here.

class NavLoginView(LoginView):
    template_name = 'article/articles.html'  # Not really used since you want login form in navbar
    form_class = AuthenticationForm

    def get_success_url(self):
        """
        Redirect to the previous page after successful login.
        If 'next' is provided in the URL (login?next=/some/path), it will use that.
        """
        return self.request.GET.get('next', reverse_lazy('article:home'))  # Redirect to the home page if no next

    def form_invalid(self, form):
        """
        If the login form is invalid, render the same page with errors.
        """
        # Add the invalid form to the context, and return the page the user was trying to access
        return self.render_to_response(self.get_context_data(login_form=form))

'''
query all Article
'''
class ArticlesListView(ListView):
    model = Article
    template_name = 'article/articles.html'
    context_object_name = 'articles'

'''
query Article whose user is currentry logged-in
'''
class PublicationsListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article/publications.html'
    context_object_name = 'articles'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

'''
query Article by pk(primary key)
'''
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = context['article']
        fav_form = AddFavouritForm()
        fav_form.initial['article'] = article

        is_fav = UserFavouriteArticle.objects.filter(user=self.request.user, article=article).first()

        context['form'] = fav_form
        context['is_fav'] = is_fav
        return context

class FavouritesListView(LoginRequiredMixin, ListView):
    template_name = 'article/favourites.html'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user).select_related('article')

class RegisterCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        # If the user is authenticated, redirect them to a different page
        if request.user.is_authenticated:
            return redirect('article:home')  # You can change 'home' to any other URL name
        return super().dispatch(request, *args, **kwargs)

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
must handle in ex02
'''
class AddFavouriteCreateView(LoginRequiredMixin, CreateView):
    model = UserFavouriteArticle
    fields = ['article']
    template_name = 'article/detail.html'
    # success_url = '/favourites'

    # Override the form_valid method to assign the author
    def form_valid(self, form):
        # Assign the current user to the form instance
        form.instance.user = self.request.user
        return super().form_valid(form)  # Try to save the favorite

    def get_success_url(self):
        # Redirect to the article detail page after successfully adding to favorites
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})
    
class RemoveFavouriteDeleteView(LoginRequiredMixin, DeleteView):
    model = UserFavouriteArticle
    # template_name = 'article/detail.html'

    def get_success_url(self):
        # Redirect to the article detail page after successfully adding to favorites
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})
    
    def get_object(self, queryset=None):
        """
        Override get_object to ensure the user can only delete their own favorites.
        """
        obj = super().get_object(queryset)
        
        # Check if the logged-in user is the owner of the favorite
        if obj.user != self.request.user:
            return HttpResponseForbidden("You are not allowed to remove this favorite.")
        
        return obj


'''
for infomation of DetailView and ListView
https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/
'''

'''
for infomation of CreateView
https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/
'''