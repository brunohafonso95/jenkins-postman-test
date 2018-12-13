# -*- coding: utf-8 -*-

from django.db import models
from pyexpat import model

# Create your models here.
TIPO_DE_TESTE=(("Manual","MANUAL"),
               ("Funcional Automatizado","FUNCIONAL AUTOMATIZADO"),
               ("Performance","PERFORMANCE"),
               ("Analise de Codigo","ANALISE DE CODIGO"),
               ("Teste de Penetração","TESTE DE PENETRAÇÃO"),
               ("Teste de API","TESTE DE API"),
               ("Segurança de Aplicação","SEGURANÇA DE APLICAÇÃO"))

CHAVES=(("Dado","DADO"),
        ("Quando","QUANDO"),
        ("Entao","ENTAO"),
        ("E","E"))

class ProjetoTesteModel(models.Model):
    nome=models.CharField(max_length=50)
    class Meta:
        verbose_name="Projeto de teste"
        verbose_name_plural="Projetos de testes"
    def __str__(self):
        return "{NAME}".format(NAME=self.nome)
    
class PlanoDeTesteModel(models.Model):
    tipo=models.CharField(max_length=50,choices=TIPO_DE_TESTE)
    projeto=models.ForeignKey(ProjetoTesteModel,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Plano de teste"
        verbose_name_plural="Planos de testes"
    def __str__(self):
        return "Plano de teste = {PLANO}:  Projeto = {PROJETO} -".format(PLANO=self.tipo,PROJETO=self.projeto.nome)
    
class FunciolidadeModel(models.Model):
    nome=models.CharField(max_length=50)
    plano=models.ForeignKey(PlanoDeTesteModel,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Funcionalidade"
        verbose_name_plural="Funcionalidades"
    def __str__(self):
        return "Funcionalidade: {NAME}".format(NAME=self.nome)
    

class StepModel(models.Model):
    chave=models.CharField(max_length=50,choices=CHAVES)
    descricao=models.CharField(max_length=50)   
    actions=models.TextField()
    
    class Meta:
        verbose_name="Step"
        verbose_name_plural="Steps"
    def __str__(self):
        return "Chave = {CHAVE}: Descrição = {NAME}".format(NAME=self.descricao,CHAVE=self.chave)
    
class CenarioModel(models.Model):
    nome=models.CharField(max_length=50)
    funcionalidade=models.ForeignKey(FunciolidadeModel,on_delete=models.CASCADE)
    steps=models.ManyToManyField(StepModel)
    class Meta:
        verbose_name="Cenario"
        verbose_name_plural="Cenarios"
    def __str__(self):
        return "Cenario: {NAME}".format(NAME=self.nome)