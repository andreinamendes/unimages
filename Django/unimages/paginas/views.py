from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import *

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
    return render(request, 'paginas/planos.html')


@login_required
def listar_planos(request):
    return Plano.objects.all().order_by(
        '-created_at')


@login_required
def cadastrar_plano(request):
    pass


@login_required
def editar_plano(request, id_plano):
    pass


@login_required
def deletar_plano(request, id_plano):
    pass


@login_required
def imagens(request):
    pass


@login_required
def listar_imagens(request):
    return Plano.objects.all().order_by(
        '-created_at')


@login_required
def cadastrar_plano(request):
    pass


@login_required
def editar_plano(request, id_plano):
    pass


@login_required
def deletar_plano(request, id_plano):
    pass
