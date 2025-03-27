from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.submit_register, name="submit_register"),
    path("login/", views.submit_login, name="submit_login"),
]
