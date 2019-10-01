from django import forms
from financas.models.conta import Conta

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = [
            'nome',
            'valor_total',
        ]

    nome = forms.CharField(max_length=250, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_total = forms.DecimalField(label="Valor Total", max_digits=9, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control col-sm-2 col-lg-2 col-xs-2 col-md-2'}))