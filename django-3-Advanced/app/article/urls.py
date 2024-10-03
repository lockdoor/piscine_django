from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import ArticlesListView, PublicationsListView, ArticleDetailView,\
    FavouritesListView, PublishCreateView

app_name = 'article'

urlpatterns = [
    path('', RedirectView.as_view(url='articles/')),
    path('articles/', ArticlesListView.as_view(), name='articles'),
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('favourites/', FavouritesListView.as_view(), name='favourites'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('publish/', PublishCreateView.as_view(), name='publish')
]
