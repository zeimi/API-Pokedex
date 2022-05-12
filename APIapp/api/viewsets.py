from rest_framework import viewsets
from APIapp.api import serializers
from APIapp import models

class PokeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PokeSerializer
    queryset = models.Pokemons.objects.all()