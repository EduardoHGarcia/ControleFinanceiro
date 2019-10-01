from django.urls import path
import financas.controllers.transacaoController as transacao
import financas.controllers.homeController as home
import financas.controllers.contaController as conta

urlpatterns = [
    path('', home.home, name='home'),
    path('transacao', transacao.home, name='home_transacao'),
    path('transacao/cadastro/', transacao.nova_transacao, name='cadastro_transacao'),
    path('transacao/alterar/<int:pk>', transacao.alterar_transacao, name='alterar_transacao'),
    path('transacao/excluir/<int:pk>', transacao.excluir_transacao, name='excluir_transacao'),
    path('conta', conta.home, name='home_conta')
]
