from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    lido = models.BooleanField(default=False)