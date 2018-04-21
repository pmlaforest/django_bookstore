from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views



from . import views

app_name = 'online_shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    
    # re_path(r'', views.error, name='error'),
]
