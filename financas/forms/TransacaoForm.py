from django.forms import ModelForm
from financas.models.transacao import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'dt_transacao', 'categoria', 'forma_pagamento', 'tipo_transacao', 'conta']
