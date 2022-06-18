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
<h1 align="center">Gifs Para Motivação da Equipe:</h1>
  
  **Beldades**
  
![takane](https://user-images.githubusercontent.com/94016306/167963728-2c3c7112-ad3f-4747-994f-efaa45c29b50.gif)
![kaguya2](https://user-images.githubusercontent.com/94016306/167966717-da4aa20d-e20b-42a8-8f76-a34e4e348f5b.gif)
&nbsp;
![ina](https://user-images.githubusercontent.com/93962428/174420052-0c049265-7bc2-47b4-918e-0f62d0bf13ec.gif)
&nbsp;
  
  **VINGADORES: ULTIMOGUS**
  
![ghostface](https://user-images.githubusercontent.com/94016306/167962626-6cea4450-eff4-4a37-bd0e-4972abca17f9.gif)
&nbsp;
![puliça](https://user-images.githubusercontent.com/94016306/167963972-c8fe6d85-9da7-44ad-856e-d6daa4853fe5.gif)
&nbsp;
![mario](https://user-images.githubusercontent.com/94016306/167964387-db491f58-1d26-41e2-8cd0-2520523f2c51.gif)
&nbsp;
![amoga](https://user-images.githubusercontent.com/94016306/167964317-33e09b17-3340-43df-bfb0-718ea1aa0964.gif)
&nbsp;
  
  **Panik**
  
![shirogane](https://user-images.githubusercontent.com/94016306/167966915-f56135f4-c6b5-4649-a17a-285999a40cec.gif)

![sam](https://user-images.githubusercontent.com/94016306/167965855-4730d313-7c32-4e75-8051-53bd71c5797d.gif)
  
![komi](https://user-images.githubusercontent.com/93962428/174412189-6c37a10f-3db0-4cd6-b639-c8f5b2e0702e.gif)
