from django.db import models

class Conta(models.Model):
    nome = models.CharField(max_length=250)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.nome