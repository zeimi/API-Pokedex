import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import Pokemon # Importando o modelo de Pokemon


def index(request):
    return render(request, 'index.html') # Renderizando a página principal da API

def inserir(request):
    return render(request, 'inserir.html') # Renderizando a página de inserir

def buscar(request): # Buscando um pokemon no banco de dados
    try:
        pokemons = []
        data = {}

        for item in list(Pokemon.objects.all()): # Listando todos os pokemons
            poke = {}
            poke['nome'] = item.nome # Adicionando o nome do pokemon na lista poke
            poke['tipo'] = item.tipo # Adicionando o tipo do pokemon na lista poke

            pokemons.append(poke) # Adicionando a lista poke na lista pokemons

        data['data'] = json.dumps(pokemons) # Convertendo a lista pokemons para json com serialização

        return JsonResponse(data) # Retornando o json com a lista de pokemons
    except Exception as error: # Caso ocorra algum erro:
        valores = {}
        print('Error', error) # Imprimindo o erro no console

        valores = {
            'Erro': 'Ocorreu um erro'
        }

        valores = json.dumps(valores)

        return JsonResponse(valores) # Exibe que ocorreu um erro no sistema


def criar(request): # Criando um pokemon no banco de dados
    try:
        if request.method == 'POST': # Se o método da requisição da pagina HTML for POST:
            nome = ''
            tipo = ''
            intermediaria = json.loads(request.body.decode('utf-8'))
            nome = intermediaria['nome']
            tipo = intermediaria['tipo']

            pokemon = Pokemon() # Criando um objeto do modelo Pokemon
            pokemon.nome = nome
            pokemon.tipo = tipo

            pokemon.save() # Salvando o objeto pokemon no banco de dados

            sucesso = {
                'nome': nome,
                'tipo': tipo
            }

            return JsonResponse(sucesso) # Retornando o json com o pokemon criado ao banco de dados
        else:
            outro = {
                'msg': 'Erro ao tentar acessar a api'
            }
            return JsonResponse(outro) # Exibe um json com uma mensagem de erro
    except Exception as error:
        print('Error', error)

        nada = {}
        nada['erro'] = 'Ocorreu algum erro no sistema'
        return JsonResponse(nada)