from django.db import models


class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
