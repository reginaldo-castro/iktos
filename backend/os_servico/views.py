from django.db.models import Q

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from .models import OrdemServico, OrdemServicoChecklist, ChecklistItem

from .serializers import (
    OrdemServicoSerializer, 
    OrdemServicoChecklistUpdateSerializer, 
    ChecklistItemSerializer,
    OrdemServicoDetalheSerializer
)


class OrdemServicoViewSet(viewsets.ModelViewSet):
    serializer_class = OrdemServicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
    
        if not user.is_authenticated:
            return OrdemServico.objects.none()

        if user.perfil == 'admin':
            return OrdemServico.objects.all()
    
        return OrdemServico.objects.filter(
            Q(status__iexact='aberto') | Q(user=user)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=True, methods=['get'], url_path='detalhe')
    def detalhe(self, request, pk=None):
        ordem_servico = self.get_object()
        serializer = OrdemServicoDetalheSerializer(ordem_servico, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def concluir(self, request, pk=None):
        ordem = self.get_object()

        if ordem.status == 'concluida':
            raise ValidationError("Ordem de serviço já está concluída.")
        
        foto = request.FILES.get('foto')

        if not ordem.foto and not foto:
            raise ValidationError("É obrigatório enviar uma foto para concluir a OS.")

        if foto:
            ordem.foto = foto

        ordem.status = 'concluida'
        ordem.save()

        return Response(
            {"detail": "Ordem de serviço concluída com sucesso."},
            status=status.HTTP_200_OK
        )
        
    @action(detail=True, methods=['post'])
    def assumir(self, request, pk=None):
        ordem = self.get_object()
        
        if ordem.status != 'aberto':
            return Response({"detail": "Esta OS já foi pega ou concluída."}, status=400)
        
        ordem.user = request.user
        ordem.status = 'em_andamento'
        ordem.save()
        
        return Response({"detail": "Você assumiu a OS com sucesso!"})


class OrdemServicoChecklistViewSet(viewsets.ModelViewSet):
    serializer_class = OrdemServicoChecklistUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch']
    
    def get_queryset(self):
        return OrdemServicoChecklist.objects.filter(
            ordem_servico__user=self.request.user
        )
    
    def perform_update(self, serializer):
        checklist = self.get_object()

        if checklist.ordem_servico.status == 'concluida':
            raise ValidationError(
                "Não é permitido alterar checklist de uma OS concluída."
            )

        serializer.save()
        

class ChecklistItemViewSet(viewsets.ModelViewSet):
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
    permission_classes = [permissions.IsAuthenticated]
