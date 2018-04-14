from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView

from . import views

app_name = 'search'
urlpatterns = [
    path('search/', views.search, name='search'),
<<<<<<< HEAD
    path('search', RedirectView.as_view(url='search/')),
    path('', views.index, name='index'),
    path('index/',  views.index, name='index'),
    re_path(r'', views.error, name='error'),
=======
    path('', views.index, name='index'),
    #path('index',  views.index, name='index'),
    path('index/', views.index, name='index'),
    #path('search', RedirectView.as_view(url='search/')),
    #re_path('', views.error, name='error'),
>>>>>>> 61dbf927ac49042a8d994b18309a6451cf43ea39
]