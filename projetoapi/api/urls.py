from django.urls import path
from . import views

urlpatterns = [ # Lista de URLs da API
    path('', views.index, name='index'), # URL da página principal da API
    path('buscar/', views.buscar, name='buscar'), # URL de buscar, que exibe todos os pokemons em JSON
    path('criar/', views.criar, name='criar'), # URL de criar, que cria um pokemon no banco de dados
    path('inserir/', views.inserir, name='inserir'), # URL de inserir, que serve para inserir um pokemon no banco de dados
    
]