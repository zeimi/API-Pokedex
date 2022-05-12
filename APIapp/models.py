from django.db import models
from uuid import uuid4

# Create your models here.


class Pokemons(models.Model):
    id_pokedex = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    shiny = models.BooleanField('Shiny')




