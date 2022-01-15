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

    # Valor: valor do plano.
    valor = models.FloatField(
        null=False,
        blank=False,
    )

    # Duracao: duracao do plano.
    duracao = models.IntegerField(
        null=False,
        blank=False,
    )

    # Pix: pix do plano.
    pix = models.TextField(
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


class Autor(models.Model):

  # Usuario: criador do Quadro (chave estrangeira).
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Banco: nome do banco.
    banco = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    agencia = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    conta = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    pix = models.CharField(
        max_length=128,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Autores'
        ordering = ('created_at',)


class Imagem(models.Model):
    # Titulo: titulo da imagem.
    titulo = models.CharField(
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
        blank=False
    )

    # Titulo: titulo da imagem.
    categoria = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    # Titulo: titulo da imagem.
    resolucao = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    # Titulo: titulo da imagem.
    formato = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    autor = models.ForeignKey(Autor, null=False, on_delete=models.CASCADE)

    # Titulo: titulo da imagem.
    link = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Imagens'
        ordering = ('created_at',)


class Imagem_favorita(models.Model):

  # Usuario: criador do Quadro (chave estrangeira).
    usuario = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    imagem = models.ForeignKey(Imagem, null=False, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Imagens_favoritas'
        ordering = ('created_at',)


class Cartao(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Banco: nome do banco.
    nome_completo = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    # Banco: nome do banco.
    numero = models.IntegerField(
        null=False,
        blank=False,
        unique=True
    )

    validade = models.DateField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Cartoes'
        ordering = ('created_at',)


class Assinante(models.Model):

    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)

    data_de_inicio = models.DateField(
        null=False,
        blank=False,
    )

    data_final = models.DateField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Assinantes'
        ordering = ('created_at',)
