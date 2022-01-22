from django.contrib import admin

# Importar e adicionar tabela.

from .models import Plano
from .models import Autor
from .models import Imagem
from .models import Cartao
from .models import Assinante
from .models import Imagem_favorita
from .models import Categoria_imagem
from .models import Formato_imagem

admin.site.register(Plano)
admin.site.register(Autor)
admin.site.register(Imagem)
admin.site.register(Cartao)
admin.site.register(Assinante)
admin.site.register(Imagem_favorita)
admin.site.register(Categoria_imagem)
admin.site.register(Formato_imagem)
