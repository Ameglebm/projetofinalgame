from django.shortcuts import render

def index(request):
    """Página principal do game_log"""
    return render(request, 'game_logs/index.html')

# Create your views here.
