from rest_framework import serializers
from .models import ProjetoTesteModel,PlanoDeTesteModel,FunciolidadeModel,StepModel,CenarioModel

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model =ProjetoTesteModel
        fields ="__all__"
        
class PlanoDeTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlanoDeTesteModel
        fields ="__all__"
        
class FunciolidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model =FunciolidadeModel
        fields ="__all__"
        
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model =StepModel
        fields ="__all__"

class CenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =CenarioModel
        fields ="__all__"
    