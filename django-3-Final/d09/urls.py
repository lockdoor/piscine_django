"""
URL configuration for d09 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from account.views import ConnectLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='account'), name="home"),
    path('account/', TemplateView.as_view(template_name = "account/account.html")),
    path('connect/', ConnectLoginView.as_view(), name="connect"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]