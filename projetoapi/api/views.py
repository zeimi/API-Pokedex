import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import Pokemon


def index(request):
    return render(request, 'index.html')

def inserir(request):
    return render(request, 'inserir.html')

def buscar(request):
    try:
        pokemons = []
        data = {}

        for item in list(Pokemon.objects.all()):
            poke = {}
            poke['nome'] = item.nome
            poke['tipo'] = item.tipo

            pokemons.append(poke)

        data['data'] = json.dumps(pokemons)

        return JsonResponse(data)
    except Exception as error:
        valores = {}
        print('Error', error)

        valores = {
            'Erro': 'Ocorreu um erro'
        }

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

            sucesso = {
                'nome': nome,
                'tipo': tipo
            }

            return JsonResponse(sucesso)
        else:
            outro = {
                'msg': 'Erro ao tentar acessar a api'
            }
            return JsonResponse(outro)
    except Exception as error:
        print('Error', error)

        nada = {}
        nada['erro'] = 'Ocorreu algum erro no sistema'
        return JsonResponse(nada)