from django.shortcuts import render, redirect
from financas.models.transacao import Transacao
from financas.models.transacao import Conta
from financas.forms.TransacaoForm import TransacaoForm

from django.http import HttpResponse

def home(request):
    transacoes = Transacao.objects.all()\
        .filter(is_deletado = False)\
        .order_by('dt_transacao')

    contas = Conta.objects.all()

    return render(request, 'home/home.html', {'transacoes': transacoes, 'contas': contas})