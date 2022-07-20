from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages 
from django.contrib.auth.models import User

def login (request):
    return render(request,'login.html')

def sing_up (request):
    return render(request, 'cadastro.html')

def validate_login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')

    usuario = auth.authenticate(request, username=username, password=password)

    if not usuario:
        #message_username_or_password_not_validate
        return redirect('/auth/login/')
    else:
        auth.login(request, usuario)
        return redirect('/profile/user/')

def validate_form(lista):

    validate = True

    for i in lista:
        if len(i.strip()) == 0:
            validate = False
            break

    return validate

def validate_password(password):
    if len(password) < 8: 
        return False
    return True

def sing_up_validate(request):
    
    firstname=request.POST.get('name')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    if not validate_form([firstname, lastname, username, email]):
        #message
        return redirect('/auth/cadastro/')

    if not validate_password(password):
        #message
        return redirect('/auth/cadastro/')
    
    if User.objects.filter(email=email).exists():
        #message
        return redirect('/auth/cadastro/')

    if User.objects.filter(username=username).exists():
        #message
        return redirect('/auth/cadastro/')

    try:
        usuario = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password
            )
        usuario.save()
    except :
        #message
        return redirect('/auth/cadastro/')

    return redirect('/auth/login/')

