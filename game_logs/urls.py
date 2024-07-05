from django.urls import path #indica o caminho uma rota
from . import views

urlpatterns = [
    path('', views.index),
]
