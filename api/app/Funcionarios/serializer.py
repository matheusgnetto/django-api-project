from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'name', 'salary', 'age', 'role', 'email', 'created_at']

class Funcionario_brlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'name', 'salary', 'salary_brl', 'age', 'role', 'email', 'created_at']