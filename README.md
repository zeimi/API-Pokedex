<h1 align="center">Projeto-API Pokémon</h1>
  
  
<h3 align="center">Passo a passo para rodar a API em seu computador:</h3>
  
1. Instale o Python em sua ultima versão: https://www.python.org/downloads/
2. Feito a instalação, instale o Django usando o comando no console python: "pip install django".
3. Clone o repositório do GitHub.

<h3 align="center">Feito isso, você já pode rodar o projeto em seu computador. Para tal, abra o terminal e execute os comandos:</h3>
  
1. cd projetoapi
2. python manage.py runserver
  
-------------------------------------------------------------------------------------------------
  
<h1 align="center">Como funciona:</h1>
  
### Criamos o app "api", que é onde devidamente se encontra a api.
na pasta api, modificamos os seguintes arquivos:
  
**models.py, views.py, urls.py.**
  
### Cada arquivo está comentado com suas devidas informações de funcionamento, mas daremos um resumo:
  
**models.py:** É onde estão as classes que representam os objetos do banco de dados.
  
**views.py:** É onde estão as funções que são chamadas pela api para armazenar ou retornar os dados.
  
**urls.py:** É onde estão as rotas da api, e define o que cada uma dessas URLs vão abrir.
  
### As rotas atuais são:
  
**url/** - Página principal
  
**url/inserir/** - Inserir um novo pokemon
  
**url/buscar/** - Listar todos os pokemons em JSON
  
**url/criar/** - Função interna da API que cria um novo pokemon no banco de dados; Caso o usuário acesse, exibirá um erro.
  
### Também criamos a pasta templates, que é onde estão os arquivos HTML que serão exibidos na nossa api.
### Nela estão os seguintes arquivos:

**index.html:** é o arquivo que será exibido na raiz da api.
  
**inserir.html:** é o arquivo que será exibido na rota /inserir.
  
----------------------------------------------------------------------
<h1 align="center">Demo publicada no youtube:</h1>
<h3 align="center">Clique na imagem para acessar o link</h3>
   
<h3 align="center">
   
[![linkimgyoutube](https://img.youtube.com/vi/LyZQ4rpKRvY/0.jpg)](https://www.youtube.com/watch?v=LyZQ4rpKRvY)
  
  </h3>
  
----------------------------------------------------------------------
<h1 align="center">Integrantes da equipe</h1>
  
<h4 align="center">
  
* Alvaro Queiroz - 201001900 
* Bruno Durão Silva - 201003074 
* Gustavo Santos Rocha - 201001215 
* Michel Gerônimo Carvalho - 201002987 
* Rodrigo Correia Santos - 201000474
  
  </h4>
  
----------------------------------------------------------------------
