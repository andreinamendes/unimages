from django.db import models
from django.contrib.auth.models import User

# Quadro: contém o quadro.

# Criar tabela
# py .\manage.py makemigrations
# py .\manage.py migrate  

class Plano(models.Model):
    # Nome: nome do plano.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    # Descricao: Descrição do plano.
    descricao = models.TextField(
        blank=True
    )

    # Valor: valor do quadro.
    valor = models.FloatField(
        null=False,
        blank=False,
    )

    # Duracao: duracao do quadro.
    duracao = models.IntegerField(
        null=False,
        blank=False,
    )

    # Pix: pix do plano.
    descricao = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Planos'
        ordering = ('created_at',)

    def __str__(self):
        return self.nome
