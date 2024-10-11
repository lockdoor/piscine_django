from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import ArticlesListView, PublicationsListView, ArticleDetailView,\
    FavouritesListView, PublishCreateView, TestDetailView

app_name = 'article'

urlpatterns = [
    path('', RedirectView.as_view(url='articles/')),
    path('articles/', ArticlesListView.as_view(), name='articles'),
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('favourites/', FavouritesListView.as_view(), name='favourites'),
    # path('add_favourtite/', AddFavouriteCreateView.as_view(), name='add-favourite'), 
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('test/<int:pk>', TestDetailView.as_view(), name="test-detail"),
    path('publish/', PublishCreateView.as_view(), name='publish')
]
