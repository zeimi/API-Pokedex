import json
from django.http import JsonResponse
from django.shortcuts import render
from api.models import Pokemon

# Create your views here.

def index(request):
    return render (request, 'index.html')

def buscar(request):
    try:
        pokemons = []
        lista = {}

        for poke in Pokemon.objects.all():
            pokelista = {}
            pokelista['nome'] = poke.nome
            pokelista['tipo'] = poke.tipo

            pokemons.append(pokelista)
        
        lista ['lista'] = json.dumps(pokemons)

        return JsonResponse(lista)
    except Exception as error:
        valores = {}
        print ('Erro', error)

        valores = {'Erro': 'Ocorreu um erro'}
        valores = json.dumps(valores)
        return JsonResponse(valores)

def criar(request):
    nome = request.POST("nome")
    tipo = request.POST("tipo")

    pokemon = Pokemon()
    pokemon.nome = nome
    pokemon.tipo = tipo

    pokemon.save()