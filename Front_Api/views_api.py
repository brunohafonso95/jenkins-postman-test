'''
Created on 12 de dez de 2018

@author: koliveirab
'''

from rest_framework import viewsets
from Front_Api.serializer import ProjetoSerializer,PlanoDeTesteSerializer,FunciolidadeSerializer,CenarioSerializer,StepSerializer
from Front_Api.models import ProjetoTesteModel,PlanoDeTesteModel,FunciolidadeModel,CenarioModel,StepModel
class ProjetoViews(viewsets.ModelViewSet):
    serializer_class =ProjetoSerializer
    queryset=ProjetoTesteModel.objects.all()
    
class PlanoDeTesteViews(viewsets.ModelViewSet):
    serializer_class =PlanoDeTesteSerializer
    queryset=PlanoDeTesteModel.objects.all()
    
class FunciolidadeViews(viewsets.ModelViewSet):
    serializer_class =FunciolidadeSerializer
    queryset=FunciolidadeModel.objects.all()
    
class CenarioViews(viewsets.ModelViewSet):
    serializer_class =CenarioSerializer
    queryset=CenarioModel.objects.all()
    
class StepViews(viewsets.ModelViewSet):
    serializer_class =StepSerializer
    queryset=StepModel.objects.all()