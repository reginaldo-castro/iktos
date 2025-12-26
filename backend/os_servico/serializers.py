from rest_framework import serializers
from .models import OrdemServico, ChecklistItem, OrdemServicoChecklist


class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ['id', 'descricao']


class OrdemServicoChecklistSerializer(serializers.ModelSerializer):
    checklist_item = ChecklistItemSerializer(read_only=True)
    
    class Meta:
        model = OrdemServicoChecklist
        fields = ['id', 'checklist_item', 'concluido']
        

class OrdemServicoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = OrdemServico
        fields = ['id', 'descricao', 'cliente', 'foto', 'status']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        usuario = self.context['request'].user
        
        ordem_servico = OrdemServico.objects.create(
            user = usuario,
            descricao=validated_data.get('descricao'),
            cliente=validated_data.get('cliente'),
            foto=validated_data.get('foto'),
            status=validated_data.get('status', 'aberto'),
        )
        
        itens = ChecklistItem.objects.all()
        for item in itens:
            OrdemServicoChecklist.objects.create(
                ordem_servico = ordem_servico,
                checklist_item=item
            )
        return ordem_servico
    
    def validate(self, attrs):
        status = attrs.get('status')
        foto = attrs.get('foto')

        if status == 'concluida':
            foto_existente = self.instance.foto if self.instance else None

            if not foto and not foto_existente:
                raise serializers.ValidationError({
                    'foto': 'Foto é obrigatória para concluir a OS.'
                })

        return attrs


class OrdemServicoDetailSerializer(serializers.ModelSerializer):
    checklist_itens = OrdemServicoChecklistSerializer(many=True, read_only=True)

    class Meta:
        model = OrdemServico
        fields = [
            'id',
            'descricao',
            'foto',
            'status',
            'checklist_itens',
            'created_at',
            'updated_at'
        ]


class OrdemServicoChecklistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServicoChecklist   
        fields = ['id', 'concluido']
        
    def validate(self, attrs):
        ordem_servico = self.instance.ordem_servico

        if ordem_servico.status == 'concluida':
            raise serializers.ValidationError(
                'Não é possível alterar o checklist de uma OS concluída.'
            )

        return attrs
        

class OrdemServicoChecklistDetalheSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(source='checklist_item.id')
    descricao = serializers.CharField(source='checklist_item.descricao', read_only=True)

    class Meta:
        model = OrdemServicoChecklist
        fields = ['id', 'descricao', 'concluido']


class OrdemServicoDetalheSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(use_url=True)
    checklist = OrdemServicoChecklistDetalheSerializer(
        source='checklist_itens',
        many=True,
        read_only=True
    )

    class Meta:
        model = OrdemServico
        fields = [
            'id',
            'descricao',
            'cliente',
            'status',
            'foto',
            'checklist'
        ]
