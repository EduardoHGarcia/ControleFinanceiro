from django.db import models
class Forma_Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Forma Pagamento"