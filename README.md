## criar ambiente virtual  
#### `python -m venv venv`  
cria um ambiente virtual na pasta `venv`.

## ativar ambiente virtual  
#### windows: `venv\Scripts\activate`  
#### linux/macOS: `source venv/bin/activate`  
lembre de ativar o ambiente antes de rodar o projeto.

## instalar django  
#### `pip install django`  
instala a versão mais recente do django.

## verificar versão do django  
#### `django-admin --version`  
confirma se o django foi instalado com sucesso.

## criar projeto django  
#### `django-admin startproject nome_do_projeto`  
substitua `nome_do_projeto` por algo significativo.

## acessar pasta do projeto  
#### `cd nome_do_projeto`  
entra na pasta criada.

## rodar servidor de desenvolvimento  
#### `python manage.py runserver`  
acesse via navegador: http://127.0.0.1:8000

## criar app django  
#### `python manage.py startapp nome_do_app`  
cria um novo app dentro do projeto.

## registrar app no projeto  
#### editar `settings.py`, adicionar `'nome_do_app'` em `INSTALLED_APPS`  
necessário para o django reconhecer o app.


# 'extends' html
## exemplo:
`{% extends "base.html" %}

{% block title %}Página 1{% endblock %}

{% block content %}
'<h2>'conteúdo da página 1'</h2>'
{% endblock %}`

## exemplo complementar
`{% extends "base.html" %}

{% block title %}Página 2{% endblock %}

{% block content %}
'<h2>'conteúdo da página 2'</h2>'
{% endblock %}`
