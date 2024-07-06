from django.shortcuts import render

def home(request):
    return render(request, 'paginas/index.html')


def cadastro(request):
    return render(request, 'paginas/cadastro.html')

# Create your views here.
