from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Forma_Pagamento)
admin.site.register(Tipo_Transacao)
admin.site.register(Conta)
# Register your models here.