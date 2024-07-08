from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from . models import Cadastro
from django.contrib import messages

def home(request):
    return render(request, 'paginas/index.html')

def cadastre(request):
    if request.method == "GET":
        return render(request, 'paginas/cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            return HttpResponse('Já existe um usuário com esse nome de usuário.')

        novo_cadastro = Cadastro(nome=nome, email=email, usuario=username, senha=password)
        novo_cadastro.save()

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    
def contato(request):
    return render(request, 'paginas/contato.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'paginas/login.html')
    else:
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)

            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')
        
@login_required(login_url="/login/")        
def plataforma(request):
    return HttpResponse('plataforma')

