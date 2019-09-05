"""controle_financas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import financas.controllers.transacaoController as transacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', transacao.home, name = 'home_transacao'),
    path('transacao/cadastro/', transacao.nova_transacao, name = 'cadastro_transacao'),
    path('transacao/alterar/<int:pk>', transacao.alterar_transacao, name = 'alterar_transacao'),
    path('transacao/excluir/<int:pk>', transacao.excluir_transacao, name = 'excluir_transacao')
]
