from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
   return render(request, 'planner/admin_dashboard.html')

def disciplinas(request):
   return render(request, 'planner/disciplinas.html')

def tarefas(request):
   return render(request, 'planner/tarefas.html')
