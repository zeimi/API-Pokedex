from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nome = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)