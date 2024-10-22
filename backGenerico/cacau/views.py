from django.shortcuts import render

from rest_framework import viewsets
from .models import (
    Cacau, Endereco, Cadastro, Produtor,
    Comercializacao, Propriedade, Producao,
    Lote, Fermentacao
)
from .serializers import (
    CacauSerializer, EnderecoSerializer, CadastroSerializer,
    ProdutorSerializer, ComercializacaoSerializer, PropriedadeSerializer,
    ProducaoSerializer, LoteSerializer, FermentacaoSerializer
)

# ViewSets para os modelos

class CacauViewSet(viewsets.ModelViewSet):
    queryset = Cacau.objects.all()
    serializer_class = CacauSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

class ComercializacaoViewSet(viewsets.ModelViewSet):
    queryset = Comercializacao.objects.all()
    serializer_class = ComercializacaoSerializer

class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer

class ProducaoViewSet(viewsets.ModelViewSet):
    queryset = Producao.objects.all()
    serializer_class = ProducaoSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class FermentacaoViewSet(viewsets.ModelViewSet):
    queryset = Fermentacao.objects.all()
    serializer_class = FermentacaoSerializer
