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
    imagens = listar_imagens(request)
    return render(request, 'paginas/index.html', {'imagens': imagens})


@login_required
def listar_imagens(request):
    return Imagem.objects.all().order_by(
        '-created_at')


@login_required
def home(request):
    imagens = listar_imagens(request)
    return render(request, 'paginas/home.html', {'imagens': imagens})


@login_required
def sobre(request):
    imagens = listar_imagens(request)
    return render(request, 'paginas/sobre.html', {'imagens': imagens})


@login_required
def contatos(request):
    imagens = listar_imagens(request)
    return render(request, 'paginas/contatos.html', {'imagens': imagens})


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
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.usuario = request.user
            plano.save()
            messages.info(request, 'Plano salvo com sucesso.')
            return redirect('/planos')
        else:
            # ser_autor
            return render(request, 'paginas/plano/cad_plano.html', {'form': form})
    else:
        form = PlanoForm()
        # ser_autor
        return render(request, 'paginas/plano/cad_plano.html', {'form': form})


@login_required
def editar_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    if request.method == 'POST':
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.usuario = request.user
            plano.save()
            messages.info(request, 'Plano salvo com sucesso.')
            return redirect('/planos')
        else:
            return render(request, 'paginas/plano/editar_plano.html', {'form': form})
    else:
        form = PlanoForm(instance=plano)
        return render(request, 'paginas/plano/editar_plano.html', {'form': form})


@login_required
def deletar_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    plano.delete()  # Deletando o plano
    messages.info(request, 'Plano deletado com sucesso.')
    return redirect('/planos')


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
            return render(request, 'paginas/plano/planos.html', {'form': form})
    else:
        form = AutorForm(instance=autor)
        return render(request, 'paginas/plano/planos.html', {'form': form})


@login_required
def deletar_autor(request):
    autor = get_object_or_404(Autor, usuario=request.user)
    autor.delete()  # Deletando o quadro
    messages.info(request, 'Autor deletado com sucesso.')
    return redirect('/home')


@login_required
def imagens(request):
    return render(request, 'paginas/imagens.html')


def listar_imagem(request, id):
    return get_object_or_404(Imagem, pk=id)  # Buscando o quadro


@login_required
def cadastrar_imagem(request):
    autor = get_object_or_404(Autor, usuario=request.user)
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.autor = autor
            imagem.save()
            messages.info(request, 'Imagem salva com sucesso.')
            return redirect('/home')
        else:
            return render(request, 'paginas/imagem/cad_imagem.html', {'form': form})
    else:
        form = ImagemForm()
        return render(request, 'paginas/imagem/cad_imagem.html', {'form': form})


@login_required
def editar_imagem(request, id_plano):
    pass


@login_required
def deletar_imagem(request, id):
    imagem = listar_imagem(id)
    imagem.delete()  # Deletando o quadro
    messages.info(request, 'Imagem deletada com sucesso.')
    return redirect('/home/')


@login_required
def cadastrar_categoria_imagem(request):
    if request.method == 'POST':
        form = CategoriaImagemForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            messages.info(request, 'Categoria salva com sucesso.')
            return redirect('/home')
        else:
            # ser_autor
            return render(request, 'paginas/categoria/cad_categoria.html', {'form': form})
    else:
        form = CategoriaImagemForm()
        # ser_autor
        return render(request, 'paginas/categoria/cad_categoria.html', {'form': form})


@login_required
def cadastrar_formato_imagem(request):
    if request.method == 'POST':
        form = FormatoImagemForm(request.POST)
        if form.is_valid():
            formato = form.save(commit=False)
            formato.save()
            messages.info(request, 'Formato salvo com sucesso.')
            return redirect('/home')
        else:
            # ser_autor
            return render(request, 'paginas/formato/cad_formato.html', {'form': form})
    else:
        form = FormatoImagemForm()
        # ser_autor
        return render(request, 'paginas/formato/cad_formato.html', {'form': form})

@login_required
def favoritar_imagem(request, id_imagem):
    usuario = request.usuario
    imagem = Imagem.objects.get(id=id_imagem)
    #imagem = listar_imagem(id)
    #imagem.delete()  # Deletando o quadro
    imagem.save()
    messages.info(request, 'Adicionada aos favoritos.')
    #return redirect('/imagem')

@login_required
def cadastrar_assinante(request):
    if request.method == 'POST':
        form = AssinanteForm(request.POST)
        if form.is_valid():
            assinante = form.save(commit=False)
            assinante.usuario = request.user
            assinante.save()
            messages.info(request, 'Parabens! Assinatura feita com sucesso!')
            return redirect('/home')
        else:
            return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
    else:
        form = AssinanteForm()
        return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
    #pass
