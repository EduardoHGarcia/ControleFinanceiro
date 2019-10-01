from django.shortcuts import render, redirect
from financas.models.transacao import Conta

from django.http import HttpResponse

def home(request):
    contas = Conta.objects.all()

    return render(request, 'conta/home.html', {'contas': contas})