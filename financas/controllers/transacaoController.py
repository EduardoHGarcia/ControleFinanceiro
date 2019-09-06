from django.shortcuts import render, redirect
from financas.models.transacao import Transacao
from financas.forms.TransacaoForm import TransacaoForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    transacoes = Transacao.objects.all()#buscar todas as informações do banco utilizando o manager do bd do banco
    return render(request, 'transacao/home.html', {'transacoes': transacoes})

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        Transacao.objects.create(**form.cleaned_data);
        return redirect('home_transacao')

    return render(request, 'transacao/form.html', {'form': form})

def alterar_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance = transacao)

    if form.is_valid():
        Transacao.objects.create(**form.cleaned_data);
        return redirect('home_transacao')

    return render(request, 'transacao/form.html', {'form': form})

def excluir_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('home_transacao')