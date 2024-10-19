from django.urls import path
from django.views.generic import RedirectView
from .views import ArticlesListView, PublicationsListView, ArticleDetailView,\
    FavouritesListView, PublishCreateView, RemoveFavouriteDeleteView,\
    AddFavouriteCreateView, NavLoginView

app_name = 'article'

urlpatterns = [
    path('', RedirectView.as_view(url='articles'), name="home"),
    path('articles/', ArticlesListView.as_view(), name='articles'),
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('favourites/', FavouritesListView.as_view(), name='favourites'),
    path('add_favourtite/', AddFavouriteCreateView.as_view(), name='add-favourite'),
    path('remove_favourtite/<int:pk>', RemoveFavouriteDeleteView.as_view(), name='remove-favourite'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('publish/', PublishCreateView.as_view(), name='publish'),
    path('nav-login/', NavLoginView.as_view(), name="nav-login")
]
