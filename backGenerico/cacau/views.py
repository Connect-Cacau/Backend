from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import (
    Cacau, Endereco, Cadastro, Produtor,
    Comercializacao, Propriedade, Producao,
    Lote, Fermentacao, Empresa, CustomUser,
)
from .serializers import (
    CacauSerializer, EnderecoSerializer, CadastroSerializer,
    ProdutorSerializer, ComercializacaoSerializer, PropriedadeSerializer,
    ProducaoSerializer, LoteSerializer, FermentacaoSerializer, EmpresaSerializer, RegisterSerializer
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
    serializer_class = RegisterSerializer

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



class EmpresaFilter(filters.FilterSet):
    tipo = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Empresa
        fields = ['tipo']

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filterset_class = EmpresaFilter
    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'email': user.email
        })
    else:
        return Response({'error': 'Credenciais inválidas'}, status=400)