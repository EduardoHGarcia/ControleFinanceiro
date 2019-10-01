from django.shortcuts import render, redirect
from financas.models.transacao import Transacao
from financas.forms.TransacaoForm import TransacaoForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    transacoes = Transacao.objects.all()\
        .filter(is_deletado = False)\
        .order_by('dt_transacao')

    return render(request, 'transacao/home.html', {'transacoes': transacoes})

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home_transacao')

    return render(request, 'transacao/form.html', {'form': form})

def alterar_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    if transacao.is_deletado:
        return redirect('home_transacao')

    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('home_transacao')

    return render(request, 'transacao/form.html', {'form': form})

def excluir_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.is_deletado = True
    transacao.save()
    return redirect('home_transacao')