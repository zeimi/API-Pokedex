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
    try:
        if request.method == 'POST':
            nome = ''
            tipo = ''
            intermediaria = json.loads(request.body.decode('utf-8'))

            nome = intermediaria['nome']
            tipo = intermediaria['tipo']

            pokemon = Pokemon()
            pokemon.nome = nome
            pokemon.tipo = tipo

            pokemon.save()

            sucesso = {'nome': nome, 'tipo': tipo}
            return JsonResponse(sucesso)

        else:
            outro = {'msg': 'Erro ao tentar acessar a api'}
            return JsonResponse(outro)

    except Exception as error:
        print('Error', error)

        nada = {}
        nada ['erro'] = 'Ocorreu algum erro no sistema'
        return JsonResponse(nada)