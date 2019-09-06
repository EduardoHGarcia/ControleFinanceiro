from django.db import models
from .categoria import Categoria
from .conta import Conta
from .forma_pagamento import Forma_Pagamento
from .tipo_transacao import Tipo_Transacao

class Transacao(models.Model):
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    dt_transacao = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    forma_pagamento = models.ForeignKey(Forma_Pagamento, on_delete=models.DO_NOTHING)
    tipo_transacao = models.ForeignKey(Tipo_Transacao, on_delete=models.DO_NOTHING)
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    is_deletado = models.BooleanField(auto_created=False, default=False)
    class Meta:
        verbose_name_plural = "Transações"
    def __str__(self):
        return self.descricao