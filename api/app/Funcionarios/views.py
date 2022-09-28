from django.shortcuts import render
from rest_framework import viewsets
from .models import Funcionario
from .serializer import FuncionarioSerializer
from .serializer import Funcionario_brlSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class Funcionario_brlViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = Funcionario_brlSerializer
