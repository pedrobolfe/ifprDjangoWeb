from django.db import models
from django.contrib.auth.models import User

class Viagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_destino = models.CharField(max_length=100)
    data_prevista_viagem = models.DateField(null=True, blank=True)
    data_prevista_retorno = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_destino} ({self.usuario.username})"