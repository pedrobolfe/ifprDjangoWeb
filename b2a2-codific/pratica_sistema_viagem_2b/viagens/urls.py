from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrar/", views.registrar, name="registrar"),
    path("login/", views.sub_login, name="sub_login"),
    path('viagens', views.cadastrar_viagem, name="cadastrar_viagem"),
    path('viagens/nova/', views.nova_viagem, name='nova_viagem'),

]
