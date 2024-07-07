from django.db import models

class Cadastro(models.Model):
    id_cadastro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    usuario = models.CharField(max_length=30, verbose_name="Usuário")
    senha = models.CharField(max_length=65, verbose_name="Senha")