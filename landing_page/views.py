from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit_register(request):
   if request.method == 'POST':
       nomeCompleto = request.POST.get('nomeCadastro')
       nomeUser = request.POST.get('userCadastro')
       email = request.POST.get('emailCadastro')
       senha = request.POST.get('passwordCadastro')
       
       print(f"Nome Completo: {nomeCompleto}, Nome: {nomeUser}, Email: {email}, Senha: {senha}")

       if nomeCompleto and nomeUser and email and senha:
           message = f"Nome Completo: {nomeCompleto}, Nome: {nomeUser}, Email: {email}, Senha: {senha}"
           return HttpResponse(message)
       else:
           return HttpResponse("Algum campo está vazio.")
   else:
       return HttpResponse("Erro ao processar.")
   
def submit_login(request):
    if request.method == 'GET':
       email = request.POST.get('loginEmail')
       senha = request.POST.get('loginPassword')
       
       print(f"Email: {email}, Senha: {senha}")

       if email and senha:
           message = f"Email: {email}, Senha: {senha}"
           return HttpResponse(message)
       else:
           return HttpResponse("Algum campo está vazio.")
    else:
       return HttpResponse("Erro ao processar.")