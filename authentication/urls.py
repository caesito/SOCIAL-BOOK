from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login' ),
    path('cadastro/', views.sing_up, name='cadastro'),
    path('singup_validate/', views.sing_up_validate, name='singup_validate'),
    path('validate_login/', views.validate_login, name='validate_login')
]