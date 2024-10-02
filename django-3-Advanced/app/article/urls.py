from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import ArticlesView

urlpatterns = [
    path("", TemplateView.as_view(template_name="article/index.html")),
    path("home/", RedirectView.as_view(url='/')),
    path('article/', ArticlesView.as_view(), name='article')
]