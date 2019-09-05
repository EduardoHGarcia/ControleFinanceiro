from django.contrib import admin
from .models.categoria import Categoria
from .models.conta import Conta
from .models.transacao import Transacao
from .models.forma_pagamento import Forma_Pagamento
from .models.tipo_transacao import Tipo_Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Forma_Pagamento)
admin.site.register(Tipo_Transacao)
admin.site.register(Conta)
# Register your models here.