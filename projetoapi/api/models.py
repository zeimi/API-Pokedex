from django.db import models


class Pokemon(models.Model): # Modelo de Pokemon para o Banco de Dados
    nome = models.TextField(max_length=255) # Nome do Pokemon, como string
    tipo = models.TextField(max_length=255) # Tipo do Pokemon, como string
