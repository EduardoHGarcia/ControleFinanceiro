from django.urls import path
import financas.controllers.transacaoController as transacao

urlpatterns = [
    path('', transacao.home, name='home_transacao'),
    path('transacao/cadastro/', transacao.nova_transacao, name='cadastro_transacao'),
    path('transacao/alterar/<int:pk>', transacao.alterar_transacao, name='alterar_transacao'),
    path('transacao/excluir/<int:pk>', transacao.excluir_transacao, name='excluir_transacao')
]
