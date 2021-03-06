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
    try:
        imagens = listar_imagens(request)
        categorias = listar_categoria_imagens(request)
        context = {'imagens': imagens, 'categorias': categorias}
        return render(request, 'paginas/index.html', context)
    except:
        redirect('/home')
        messages.warning(request, 'Nenhuma imagem encontrada.')


@login_required
def listar_imagens(request):
    try:
        imagens = list(Imagem.objects.all())
        shuffle(imagens)
        return imagens
    except:
        redirect('/home')
        messages.warning(request, 'Nenhuma imagem encontrada.')


@login_required
def listar_imagens_favoritas(request):
    try:
        imagens = list(Imagem_favorita.objects.all())
        shuffle(imagens)
        return imagens
    except:
        redirect('/home')
        messages.warning(request, 'Nenhuma imagem encontrada.')


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
    imagens = listar_imagens(request)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens, 'categorias': categorias, 'planos': planos}
    return render(request, 'paginas/plano/planos.html', context)


@login_required
def listar_planos(request):
    try:
        return Plano.objects.all().order_by(
            '-created_at')
    except:
        redirect('/home')
        messages.warning(request, 'Nenhum plano encontrado.')


def plano(request, id):
    try:
        plano = get_object_or_404(Plano, pk=id)
        imagens = listar_imagens(request)
        categorias = listar_categoria_imagens(request)
        context = {'imagens': imagens,
                   'categorias': categorias, 'plano': plano}
        return render(request, 'paginas/plano/plano.html', context)
    except:
        redirect('/home')
        messages.warning(request, 'Plano n??o encontado.')


@login_required
def cadastrar_plano(request):
    try:
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
    except:
        redirect('/home')
        messages.warning(request, 'Erro ao cadastrar plano.')


@login_required
def editar_plano(request, id):
    try:
        plano = get_object_or_404(Plano, pk=id)
    except:
        redirect('/home')
        messages.warning(request, 'Plano n??o encontado.')

    try:
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
    except:
        redirect('/home')
        messages.warning(request, 'Plano n??o editado.')


@login_required
def deletar_plano(request, id):
    try:
        plano = get_object_or_404(Plano, pk=id)
    except:
        redirect('/home')
        messages.warning(request, 'Plano n??o encontado.')
    plano.delete()  # Deletando o plano
    messages.info(request, 'Plano deletado com sucesso.')
    return redirect('/planos')


@login_required
def autores(request):
    pass


@login_required
def autor(request):
    pass


@login_required
def listar_autores(request):
    pass


def listar_autor(request, id):
    pass  # Buscando o quadro


@login_required
def cadastrar_autor(request):
    try:
        if request.method == 'POST':
            form = AutorForm(request.POST)
            if form.is_valid():
                autor = form.save(commit=False)
                autor.usuario = request.user
                try:
                    autor.save()
                    messages.info(request, 'Autor salvo com sucesso.')
                except:
                    messages.warning(request, 'Voc?? j?? ?? autor.')
                return redirect('/home')
            else:
                return render(request, 'paginas/autor/ser_autor.html', {'form': form})
        else:
            form = AutorForm()
            return render(request, 'paginas/autor/ser_autor.html', {'form': form})
    except:
        redirect('/home')
        messages.warning(request, 'Ouve algum erro no cadastro.')


@login_required
def editar_autor(request):
    try:
        autor = get_object_or_404(Autor, usuario=request.user)
    except:
        redirect('/home')
        messages.warning(request, 'Autor n??o encontado.')
    try:
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
    except:
        redirect('/home')
        messages.warning(request, 'Houve um erro ao editar o autor.')


@login_required
def deletar_autor(request):
    try:
        autor = get_object_or_404(Autor, usuario=request.user)
    except:
        redirect('/home')
        messages.warning(request, 'Autor n??o encontado.')
    autor.delete()  # Deletando o quadro
    messages.info(request, 'Autor deletado com sucesso.')
    return redirect('/home')


@login_required
def imagem(request, id):
    try:
        imagem = get_object_or_404(Imagem, id=id)
    except:
        redirect('/home')
        messages.warning(request, 'Imagem n??o encontada.')
    return render(request, 'paginas/imagem/imagem.html', {'imagem': imagem})


def listar_imagem(request, id):
    try:
        return get_object_or_404(Imagem, pk=id)
    except:
        redirect('/home')
        messages.warning(request, 'Imagem n??o encontada.')


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
        messages.warning(
            request, 'Voc?? precisa se cadastrar como um autor para cadastrar uma imagem.')
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
    try:
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
    except:
        redirect('/home')
        messages.warning(request, 'Houve um erro ao cadastrar a categoria.')


@login_required
def cadastrar_formato_imagem(request):
    try:
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
    except:
        redirect('/home')
        messages.warning(request, 'Formato n??o cadastrado.')


@login_required
def favoritar_imagem(request, id):
    try:
        imagem = get_object_or_404(Imagem, pk=id)
    except:
        messages.warning(request, 'Imagem n??o encontada.')
        return redirect('/home')
    try:
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
                messages.info(request, 'J?? foi salva.')
                return redirect('/home')
    except:
        messages.warning(request, 'Imagem j?? est?? favoritada.')
        return redirect('/home')


@login_required
def desfavoritar_imagem(request, id):
    try:
        imagem = get_object_or_404(Imagem_favorita, pk=id)
        imagem.delete()  # Deletando o quadro
        messages.info(request, 'J?? foi salvo.')
    except:
        messages.warning(request, 'Imagem n??o encontada.')
    return redirect('/imagens_favoritas')


@login_required
def imagens_favoritas(request):
    imagens_favoritas = listar_imagens_favoritas(request)
    return render(request, 'paginas/imagem/imagens_favoritas.html', {'imagens_favoritas': imagens_favoritas})


@login_required
def cadastrar_assinante(request):
    try:
        if request.method == 'POST':
            form = AssinanteForm(request.POST)
            if form.is_valid():
                assinante = form.save(commit=False)
                assinante.usuario = request.user
                assinante.data_de_inicio = date.today()
                assinante.data_final = date.today() + timedelta(days=364)
                try:
                    assinante.save()
                    messages.info(
                    request, 'Parabens! Assinatura feita com sucesso!')
                except:
                    messages.warning(request, 'Voc?? j?? ?? assinante.')
                return redirect('/home')
            else:
                return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
        else:
            form = AssinanteForm()
            return render(request, 'paginas/assinante/ser_assinante.html', {'form': form})
    except:
        redirect('/home')
        messages.warning(request, 'Houve um erro ao cadastrar o assinante.')


@login_required
def estudante(request):
    try:
        if request.method == 'POST':
            form = EstudanteForm(request.POST, request.FILES)
            if form.is_valid():
                estudante = form.save(commit=False)
                estudante.usuario = request.user
                try:
                    estudante = estudante.save()
                    messages.info(request, 'Estudante salvo com sucesso.')
                except:
                    messages.warning(request, 'Voc?? j?? ?? estudante.')
                return redirect('/home')
            else:
                return render(request, 'paginas/estudante/sou_estudante.html', {'form': form})
        else:
            form = EstudanteForm()
            return render(request, 'paginas/estudante/sou_estudante.html', {'form': form})
    except:
        redirect('/home')
        messages.warning(
            request, 'O plano de estudante n??o p??de ser contratado.')


@login_required
def imagens_categorias(request, id):
    try:
        categoria = get_object_or_404(Categoria_imagem, pk=id)
    except:
        redirect('/home')
        messages.warning(request, 'Categoria n??o encontada.')
    imagens = list(Imagem.objects.all().filter(categoria=categoria))
    shuffle(imagens)
    categorias = listar_categoria_imagens(request)
    context = {'imagens': imagens,
               'categoria': categoria, 'categorias': categorias}
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
