from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages

from viagens.models import Viagem

def index(request):
    return render(request,'viagens/index.html')


def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('registerName')
        senha = request.POST.get('registerPassword')
        email = request.POST.get('registerEmail')

        print(f"Nome: {nome}, Email: {email}, Senha: {senha}")

        if nome and senha and email:
            user = User.objects.create_user(
                username=nome,
                password=senha,
                email=email
            )
            user.save()
            return HttpResponse("Usuário registrado com sucesso.")            
        else:
           return HttpResponse("Algum campo está vazio.")

    else:
       return HttpResponse("Erro ao processar.")
   
def sub_login(request):
    if request.method == 'POST':
        username = request.POST.get('loginUser')
        senha = request.POST.get('loginPassword')

        print(f"{username}={senha}")

        if username and senha:
            user = authenticate(username=username, password=senha)
            if user is not None:
                login(request, user)
                print("Usuário logado com sucesso.")            
                return redirect('cadastrar_viagem')
            else:
                print("Credenciais inválidas. Verifique e tente novamente.")
                messages.error(request, "Credenciais inválidas. Verifique e tente novamente.")
        else:
            messages.error(request, "Preencha todos os campos.")
        return redirect('index')  # redireciona de volta para a tela de login
    else:
        messages.error(request, "Erro ao processar requisição.")
        return redirect('index')
    
@login_required(login_url='index')
def cadastrar_viagem(request):
    return render(request, 'viagens/nova_viagem.html')

@login_required(login_url='index')
def nova_viagem(request):
    print("entrou aqui")
    if request.method == 'POST':
        user = request.user
        destino = request.POST.get('destino')
        ida = request.POST.get('data_ida')
        volta = request.POST.get('data_volta')


        if user and destino and ida and volta:
            viagem = Viagem.objects.create(
                usuario=user,
                nome_destino=destino,
                data_prevista_viagem=ida,
                data_prevista_retorno =volta
            )
            viagem.save()
            return HttpResponse("Usuário registrado com sucesso.")            
        else:
           return HttpResponse("Algum campo está vazio.")

    else:
        return HttpResponse(request, "Erro ao processar.")