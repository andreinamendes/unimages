from time import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import date, timedelta
from .models import *
from .forms import *
from random import shuffle

# Primeira tela.

# Criar views


@login_required
def index(request):
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categorias': categorias}
    return render(request, 'paginas/index.html', context)


@login_required
def listar_imagens(request):
    imagens = list(Imagem.objects.all())
    shuffle(imagens)
    return imagens


@login_required
def listar_imagens_favoritas(request):
    imagens = list(Imagem_favorita.objects.all())
    shuffle(imagens)
    return imagens


@login_required
def listar_categoria_imagens(request):
    return Categoria_imagem.objects.all().order_by(
        '-created_at')


@login_required
def home(request):
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categorias': categorias}
    return render(request, 'paginas/home.html', context)


@login_required
def sobre(request):
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categorias': categorias}
    return render(request, 'paginas/sobre.html', context)


@login_required
def contatos(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Contato salvo com sucesso.')
            redirect('/home')
    form = ContatoForm()
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categorias': categorias, 'form': form}
    return render(request, 'paginas/contatos.html', context)


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
def imagem(request, id):
    imagem = get_object_or_404(Imagem, id=id)
    return render(request, 'paginas/imagem/imagem.html', {'imagem': imagem})


def listar_imagem(request, id):
    return get_object_or_404(Imagem, pk=id)  # Buscando o quadro


@login_required
def cadastrar_imagem(request):
    try:
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
    except:
        messages.warning(request, 'Você precisa se cadastrar como um autor para cadastrar uma imagem.')
        return redirect('/home')

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
def favoritar_imagem(request, id):
    imagem = get_object_or_404(Imagem, id=id)
    if request.method == 'POST':
        form = ImagemFavoritaForm(request.POST)
        if form.is_valid():
            imagem_favorita = form.save(commit=False)
            imagem_favorita.imagem = imagem
            imagem_favorita.usuario = request.user
            imagem_favorita.save()
            messages.info(request, 'salva com sucesso.')
            return redirect('/home')
        else:
            messages.info(request, 'Já foi salva.')
            return redirect('/home')


@login_required
def imagens_favoritas(request):
    imagens_favoritas = listar_imagens_favoritas(request)
    return render(request, 'paginas/imagem/imagens_favoritas.html', {'imagens_favoritas': imagens_favoritas})

@login_required
def cadastrar_assinante(request):
    if request.method == 'POST':
        form = AssinanteForm(request.POST)
        if form.is_valid():
            assinante = form.save(commit=False)
            assinante.usuario = request.user
            assinante.data_de_inicio = date.today()
            assinante.data_final = date.today() + timedelta(days=364)
            assinante.save()
            messages.info(request, 'Parabens! Assinatura feita com sucesso!')
            return redirect('/home')
        else:
            return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
    else:
        form = AssinanteForm()
        return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
    # pass


@login_required
def estudante(request):
    #plano = get_object_or_404(Plano, nome="Estudante")
    if request.method == 'POST':
        form = EstudanteForm(request.POST, request.FILES)
        if form.is_valid():
            estudante = form.save(commit=False)
            estudante.usuario = request.user
            #estudante = estudante.plano = plano
            estudante = estudante.save()
            messages.info(request, 'Estudante salvo com sucesso.')
            return redirect('/home')
        else:
            return render(request, 'paginas/estudante/sou_estudante.html', {'form': form})
    else:
        form = EstudanteForm()
        return render(request, 'paginas/estudante/sou_estudante.html', {'form': form})


@login_required
def imagens_categorias(request, id):
    categoria = get_object_or_404(Categoria_imagem, pk=id)
    imagens = list(Imagem.objects.all().filter(categoria=categoria))
    shuffle(imagens)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categoria': categoria, 'categorias': categorias}
    return render(request, 'paginas/categoria/imagens_categoria.html', context)

@login_required
def sucesso(request):
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    msg = 'jjj'
    context = {'imagens': imagens, 'categorias': categorias, 'msg': msg}
    return render(request, 'paginas/sucesso/sucesso.html', context)

@login_required
def download_imagem(request, id):
    pass

@login_required
def erro(request):
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    msg = 'kkk'
    context = {'imagens': imagens, 'categorias': categorias, 'msg': msg}
    return render(request, 'paginas/erro/erro.html', context)
