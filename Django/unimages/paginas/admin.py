from django.contrib import admin

# Importar e adicionar tabela.

from .models import *

admin.site.register(Plano)
admin.site.register(Autor)
admin.site.register(Imagem)
admin.site.register(Cartao)
admin.site.register(Assinante)
admin.site.register(Imagem_favorita)
admin.site.register(Categoria_imagem)
admin.site.register(Formato_imagem)
admin.site.register(Estudante)
admin.site.register(Estabelecimento_de_ensino)
admin.site.register(Contato)
