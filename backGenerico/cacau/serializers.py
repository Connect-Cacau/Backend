from rest_framework import serializers
from .models import (
    Cacau, Endereco, Cadastro, Produtor,
    Comercializacao, Propriedade, Producao,
    Lote, Fermentacao
)

class CacauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cacau
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'

class ProdutorSerializer(serializers.ModelSerializer):
    cadastroProd = serializers.PrimaryKeyRelatedField(
        queryset=Cadastro.objects.all()
    )
    
    class Meta:
        model = Produtor
        fields = '__all__'

class ComercializacaoSerializer(serializers.ModelSerializer):
    prodCom = serializers.PrimaryKeyRelatedField(
        queryset=Produtor.objects.all()
    )
    
    class Meta:
        model = Comercializacao
        fields = '__all__'

class PropriedadeSerializer(serializers.ModelSerializer):
    endProp = serializers.PrimaryKeyRelatedField(
        queryset=Endereco.objects.all()
    )

    class Meta:
        model = Propriedade
        fields = '__all__'

class ProducaoSerializer(serializers.ModelSerializer):
    propProducao = serializers.PrimaryKeyRelatedField(
        queryset=Propriedade.objects.all()
    )
    
    class Meta:
        model = Producao
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    loteProd = serializers.PrimaryKeyRelatedField(
        queryset=Producao.objects.all()
    )
    
    class Meta:
        model = Lote
        fields = '__all__'

class FermentacaoSerializer(serializers.ModelSerializer):
    loteFerm = serializers.PrimaryKeyRelatedField(
        queryset=Lote.objects.all()
    )
    
    class Meta:
        model = Fermentacao
        fields = '__all__'
