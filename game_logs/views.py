from django.shortcuts import render

def home(request):
    return render(request, 'paginas/index.html')

def cadastro(request):
    return render(request, 'paginas/cadastro.html')

def contato(request):
    return render(request, 'paginas/contato.html')

def login(request):
    return render(request, 'paginas/login.html')

# Create your views here.
