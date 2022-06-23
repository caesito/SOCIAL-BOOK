from django.urls import path
from . import views

urlpatterns = [
    path('authentication/login', views.login, name='Login' ),
    path('authentication/singup', views.sing_up, name='Cadastro')
]