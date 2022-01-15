from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from .forms import *

# Primeira tela.

# Criar views


@login_required
def index(request):
    return render(request, 'paginas/index.html')


@login_required
def home(request):
    return render(request, 'paginas/home.html')


@login_required
def sobre(request):
    return render(request, 'paginas/sobre.html')


@login_required
def contatos(request):
    return render(request, 'paginas/contatos.html')


@login_required
def planos(request):
    planos = listar_planos(request)
    return render(request, 'paginas/plano/planos.html', {'planos': planos})


@login_required
def listar_planos(request):
    return Plano.objects.all().order_by(
        '-created_at')


def plano(request, id):
    plano = get_object_or_404(Plano, pk=id)
    return render(request, 'paginas/plano/plano.html', {'plano': plano})


@login_required
def cadastrar_plano(request):
    pass


@login_required
def editar_plano(request, id):
    pass


@login_required
def deletar_plano(request, id_plano):
    pass


@login_required
def autores(request):
    return render(request, 'paginas/autores.html')


@login_required
def autor(request):

    return render(request, 'paginas/autor/autor.html')


@login_required
def listar_autores(request):
    pass


def listar_autor(request, id):
    return get_object_or_404(Autor, pk=id)  # Buscando o quadro


@login_required
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.usuario = request.user
            autor.save()
            messages.info(request, 'Autor salvo com sucesso.')
            return redirect('/home')
        else:
            return render(request, 'paginas/autor/ser_autor.html', {'form': form})
    else:
        form = AutorForm()
        return render(request, 'paginas/autor/ser_autor.html', {'form': form})


@login_required
def editar_autor(request):
    autor = get_object_or_404(Autor, usuario=request.user)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.usuario = request.user
            autor.save()
            messages.info(request, 'Autor salvo com sucesso.')
            return redirect('/home')
        else:
            return render(request, 'paginas/autor/ser_autor.html', {'form': form})
    else:
        form = AutorForm(instance=autor)
        return render(request, 'paginas/autor/ser_autor.html', {'form': form})


@login_required
def deletar_autor(request):
    autor = get_object_or_404(Autor, usuario=request.user)
    autor.delete()  # Deletando o quadro
    messages.info(request, 'Autor deletado com sucesso.')
    return redirect('/home')


@login_required
def imagens(request):
    return render(request, 'paginas/imagens.html')


@login_required
def listar_imagens(request):
    pass


def listar_imagem(request, id):
    return get_object_or_404(Imagem, pk=id)  # Buscando o quadro


@login_required
def cadastrar_imagem(request):
    pass


@login_required
def editar_imagem(request, id_plano):
    pass


@login_required
def deletar_imagem(request, id):
    imagem = listar_imagem(id)
    imagem.delete()  # Deletando o quadro
    messages.info(request, 'Imagem deletada com sucesso.')
    return redirect('/home/')
