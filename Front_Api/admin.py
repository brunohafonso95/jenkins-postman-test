from django.contrib import admin
from .models import FunciolidadeModel,PlanoDeTesteModel,ProjetoTesteModel,StepModel,CenarioModel
# Register your models here.
class FunciolidadeModeladmin(admin.ModelAdmin):
    list_display="__all__"
    
admin.site.register(FunciolidadeModel)

class PlanoDeTesteModelamdin(admin.ModelAdmin):
    list_display="__all__"
    
admin.site.register(PlanoDeTesteModel)

class ProjetoTesteModeladmin(admin.ModelAdmin):
    list_display="__all__"
    
admin.site.register(ProjetoTesteModel)

class StepModeladmin(admin.ModelAdmin):
    list_display="__all__"
    
admin.site.register(StepModel)

class CenarioModeladmin(admin.ModelAdmin):
    list_display="__all__"
    
admin.site.register(CenarioModel)

