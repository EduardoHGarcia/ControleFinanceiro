from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Forma_Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Forma Pagamento"

class Tipo_Transacao(models.Model):
    nome = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Tipo Transações"
    def __str__(self):
        return self.nome


class Conta(models.Model):
    nome = models.CharField(max_length=250)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.nome

#teste
class Transacao(models.Model):
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    dt_transacao = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    forma_pagamento = models.ForeignKey(Forma_Pagamento, on_delete=models.DO_NOTHING)
    tipo_transacao = models.ForeignKey(Tipo_Transacao, on_delete=models.DO_NOTHING)
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    is_deletado = models.BooleanField(auto_created=False)
    class Meta:
        verbose_name_plural = "Transações"
    def __str__(self):
        return self.descricao