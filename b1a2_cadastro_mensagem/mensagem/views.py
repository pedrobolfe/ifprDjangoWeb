from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mensagem_enviada(request):
   if request.method == 'POST':
       nome = request.POST.get('nome')
       mensagem = request.POST.get('mensagem')
       
       print(f"Obrigado, {nome}! Sua mensagem foi: {mensagem}")

       if nome and mensagem:
           message = f"Obrigado, {nome}! Sua mensagem foi: {mensagem}"
           return HttpResponse(message)
       else:
           return HttpResponse("Algum campo está vazio.")
   else:
       return HttpResponse("Erro ao processar.")

def inicio(request):
   
   return render(request, 'base.html')

def sobre(request):
   return render(request, 'sobre.html')

def ajuda(request):
   return render(request, 'ajuda.html')
