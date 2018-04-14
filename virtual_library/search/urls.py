from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView

from . import views

app_name = 'search'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    #path('index',  views.index, name='index'),
    path('index/', views.index, name='index'),
    #path('search', RedirectView.as_view(url='search/')),
    #re_path('', views.error, name='error'),
]