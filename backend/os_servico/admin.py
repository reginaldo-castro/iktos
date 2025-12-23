from django.contrib import admin
from .models import OrdemServico, ChecklistItem, OrdemServicoChecklist


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
    list_filter = ('status',)
    search_fields = ('descricao',)


@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    search_fields = ('descricao',)


@admin.register(OrdemServicoChecklist)
class OrdemServicoChecklistAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'checklist_item', 'concluido')
    list_filter = ('concluido',)
