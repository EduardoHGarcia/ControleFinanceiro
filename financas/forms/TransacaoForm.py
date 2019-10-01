from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from financas.models.categoria import Categoria
from financas.models.forma_pagamento import Forma_Pagamento
from financas.models.tipo_transacao import Tipo_Transacao
from financas.models.conta import Conta
from financas.models.transacao import Transacao

def validacao_data_mes_ano_passado(value):
    today = date.today()
    if (value.month < today.month and value.year == today.year) or value.year < today.year:
        raise ValidationError('A data da transação não pode ser anterior a este mês')

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = [
            'descricao',
            'valor',
            'dt_transacao',
            'categoria',
            'forma_pagamento',
            'tipo_transacao',
            'conta'
        ]

    descricao = forms.CharField(max_length=250, label='Descrição',
                                widget=forms.Textarea(
                                    attrs=
                                    {'class': 'form-control',
                                     'rows': 2
                                     }
                                ))
    valor = forms.DecimalField(label="Valor", max_digits=9, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control col-sm-2 col-lg-2 col-xs-2 col-md-2'}))
    dt_transacao = forms.DateField(label="Data", widget=forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date', 'class': 'form-control col-sm-2 col-lg-2 col-xs-2 col-md-2'}), validators=[validacao_data_mes_ano_passado])
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label = "Categoria", widget=forms.Select(attrs={'class': 'form-control bootstrap-select col-sm-3 col-lg-3 col-xs-3 col-md-3'}))
    forma_pagamento = forms.ModelChoiceField(queryset=Forma_Pagamento.objects.all(), label = "Forma de Pagamento", widget=forms.Select(attrs={'class': 'form-control bootstrap-select col-sm-3 col-lg-3 col-xs-3 col-md-3'}))
    tipo_transacao = forms.ModelChoiceField(queryset=Tipo_Transacao.objects.all(), label = "Tipo de Transação", widget=forms.Select(attrs={'class': 'form-control bootstrap-select col-sm-3 col-lg-3 col-xs-3 col-md-3'}))
    conta = forms.ModelChoiceField(queryset=Conta.objects.all(), label = "Conta", widget=forms.Select(attrs={'class': 'form-control bootstrap-select col-sm-3 col-lg-3 col-xs-3 col-md-3'}))