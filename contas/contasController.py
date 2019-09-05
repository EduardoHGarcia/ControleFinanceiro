from django.shortcuts import render
from .models import Transacao

# Create your views here.
from django.http import HttpResponse

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()#buscar todas as informações do banco utilizando o manager do bd do banco
    return render(request, 'contas/home.html', data)