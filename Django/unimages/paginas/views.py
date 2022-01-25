from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Primeira tela.


def index(request):
    return render(request, 'paginas/index.html')


def home(request):
    return render(request, 'paginas/home.html')


def sobre(request):
    return render(request, 'paginas/sobre.html')


def contatos(request):
    return render(request, 'paginas/contatos.html')
