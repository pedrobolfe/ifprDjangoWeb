from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path('mensagem-enviada/', views.mensagem_enviada, name='mensagem_enviada'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda')
]
