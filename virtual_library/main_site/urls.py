from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views



from . import views

app_name = 'main_site'
urlpatterns = [
    path('search/', views.search, name='search'),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.login, {'template_name': 'main_site/signin_form.html'}, name='signin'),
    path('signin/auth/', views.auth, name='auth'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('search/<keyword>/', views.search, name='search'),
    path('', views.index, name='index'),
    path('index/',  RedirectView.as_view(url='')),
    path('book/<int:book_id>/', views.get_info, name='get_info'),
    # re_path(r'', views.error, name='error'),
]
