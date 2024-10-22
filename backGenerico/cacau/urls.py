from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CacauViewSet, EnderecoViewSet, CadastroViewSet, ProdutorViewSet,
    ComercializacaoViewSet, PropriedadeViewSet, ProducaoViewSet,
    LoteViewSet, FermentacaoViewSet
)

router = DefaultRouter()
router.register(r'cacau', CacauViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'cadastro', CadastroViewSet)
router.register(r'produtor', ProdutorViewSet)
router.register(r'comercializacao', ComercializacaoViewSet)
router.register(r'propriedade', PropriedadeViewSet)
router.register(r'producao', ProducaoViewSet)
router.register(r'lote', LoteViewSet)
router.register(r'fermentacao', FermentacaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]