from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView

from . import views

app_name = 'main_site'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('search', RedirectView.as_view(url='search/')),
    path('', views.index, name='index'),
    path('index/',  views.index, name='index'),
    re_path(r'', views.error, name='error'),
]