from django.db import models
class Tipo_Transacao(models.Model):
    nome = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Tipo Transações"
    def __str__(self):
        return self.nome