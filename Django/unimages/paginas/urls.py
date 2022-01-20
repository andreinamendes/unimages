from django.urls import path

from . import views

app_name = 'paginas'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('sobre', views.sobre, name='sobre'),
    path('contatos', views.contatos, name='contatos'),
    path('cadastrar_autor/',
         views.cadastrar_autor, name='cadastrar_autor'),
    path('editar_autor/',
         views.editar_autor, name='editar_autor'),
    path('deletar_autor/',
         views.deletar_autor, name='deletar_autor'),
    path('autor/<int:id>/',
         views.autor,
         name='autor'),
    path('planos', views.planos, name='planos'),
    path('cadastrar_plano/',
         views.cadastrar_plano, name='cadastrar_plano'),
    path('editar_plano/<int:id>/',
         views.editar_plano, name='editar_plano'),
    path('deletar_plano/<int:id>/',
         views.deletar_plano, name='deletar_plano'),
    path('plano/<int:id>/',
         views.plano,
         name='autor'),
    path('cadastrar_imagem/',
         views.cadastrar_imagem, name='cadastrar_imagem'),
]
