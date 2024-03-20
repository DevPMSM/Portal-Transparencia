from django.db import models

#Cria o modelo que representa os dados do crud
class Informacoes(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=16)
    relatorio = models.TextField(default="Relatório padrão")

    def __str__(self) -> str:
        return self.nome, self.cpf