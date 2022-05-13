from django.db import models

# Create your models here.

class TipoPokemon(models.Model):
    tipo = models.TextField()
    imagemtipo = models.ImageField()

class Pokemon(models.Model):
    img = models.ImageField()
    nome = models.TextField(max_length=255)
    numero = models.IntegerField()
    tipos = models.ManyToManyField(TipoPokemon)
    habilidade = models.TextField(max_length=255)
    peso = models.FloatField()
    altura = models.FloatField()
    descricao = models.TextField(max_length=255)
    shinyimg = models.ImageField()
