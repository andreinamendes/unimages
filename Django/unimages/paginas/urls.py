from django.urls import path

from . import views

app_name = 'paginas'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('sobre', views.sobre, name='sobre'),
    path('contatos', views.contatos, name='contatos'),
]
