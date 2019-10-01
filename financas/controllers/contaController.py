from django.shortcuts import render, redirect
from financas.models.transacao import Conta
from financas.forms.ContaForm import ContaForm

from django.http import HttpResponse

def home(request):
    contas = Conta.objects.all()

    return render(request, 'conta/home.html', {'contas': contas})

def nova_conta(request):
    form = ContaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home_conta')

    return render(request, 'conta/form.html', {'form': form})

def alterar_conta(request, pk):
    conta = Conta.objects.get(pk=pk)
    form = ContaForm(request.POST or None, instance=conta)

    if form.is_valid():
        form.save()
        return redirect('home_conta')

    return render(request, 'conta/form.html', {'form': form})

def excluir_conta(request, pk):
    conta = Conta.objects.get(pk=pk)
    conta.delete()
    return redirect('home_conta')