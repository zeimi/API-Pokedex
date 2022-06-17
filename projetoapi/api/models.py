from django.db import models


class Pokemon(models.Model):
    nome = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
