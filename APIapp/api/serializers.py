from rest_framework import serializers
from APIapp import models

class PokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemons
        fields = '__all__'