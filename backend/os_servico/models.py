from django.conf import settings
from django.db import models


class ChecklistItem(models.Model):
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descricao
    

class OrdemServico(models.Model):
    STATUS_CHOICES = (
        ('aberto', 'Aberta'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ordens_servico'
    )

    descricao = models.TextField(verbose_name='Descrição da atividade')

    foto = models.ImageField(
        upload_to='ordens_servico/',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='aberto'
    )
    
    checklist = models.ManyToManyField(ChecklistItem, through="OrdemServicoChecklist", related_name="ordens_servico")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'OS #{self.id}'


class OrdemServicoChecklist(models.Model):
    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,
        related_name='checklist_itens'
    )

    checklist_item = models.ForeignKey(
        ChecklistItem,
        on_delete=models.CASCADE
    )

    concluido = models.BooleanField(default=False)

    class Meta:
        unique_together = ('ordem_servico', 'checklist_item')

