from django.db import models
#from django.contrib.auth.models import CustomUser

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
        max_length=258,
        null=False,
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
        blank=True,
        unique=True
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
    usuario = models.OneToOneField(
        'usuarios.CustomUser', on_delete=models.CASCADE)

    # Banco: nome do banco.
    banco = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    agencia = models.CharField(
        max_length=4,
        null=False,
        blank=False,
    )

    conta = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        unique=True
    )

    pix = models.CharField(
        max_length=128,
        unique=True,
        blank=True,
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

    def __str__(self):
        return self.usuario.username


class Categoria_imagem(models.Model):
    # Banco: nome do banco.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Categorias'
        ordering = ('created_at',)

    def __str__(self):
        return self.nome


class Formato_imagem(models.Model):
    # Banco: nome do banco.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Categorias'
        ordering = ('created_at',)

    def __str__(self):
        return self.nome


class Estabelecimento_de_ensino(models.Model):
    # Banco: nome do banco.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Estabelecimentos de ensino'
        ordering = ('created_at',)

    def __str__(self):
        return self.nome


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
        max_length=258,
        blank=True
    )

    # Valor: valor do quadro.
    valor = models.FloatField(
        null=False,
        blank=False
    )

    # Titulo: titulo da imagem.
    categoria = models.ForeignKey(
        Categoria_imagem, null=False, on_delete=models.CASCADE)

    # Titulo: titulo da imagem.
    resolucao = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )

    # Titulo: titulo da imagem.
    formato = models.ForeignKey(
        Formato_imagem, null=False, on_delete=models.CASCADE)

    autor = models.ForeignKey(Autor, null=False, on_delete=models.CASCADE)

    arquivo = models.ImageField(upload_to='imagens/', null=False, blank=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Imagens'
        ordering = ('created_at',)

    def __str__(self):
        return self.titulo


class Imagem_favorita(models.Model):

  # Usuario: criador do Quadro (chave estrangeira).
    usuario = models.ForeignKey(
        'usuarios.CustomUser', null=False, on_delete=models.CASCADE)
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

    usuario = models.ForeignKey(
        'usuarios.CustomUser', on_delete=models.CASCADE)

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

    usuario = models.OneToOneField(
        'usuarios.CustomUser', on_delete=models.CASCADE)

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


class Estudante(models.Model):

    usuario = models.OneToOneField(
        'usuarios.CustomUser', on_delete=models.CASCADE)

    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)

    estabelecimento_de_ensino = models.ForeignKey(
        Estabelecimento_de_ensino, on_delete=models.CASCADE)

    data_final = models.DateField(
        null=False,
        blank=False,
    )

    comprovante_de_matricula = models.FileField(
        upload_to='arquivos/')

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Estudantes'
        ordering = ('created_at',)

    def __str__(self):
        return self.usuario.username
