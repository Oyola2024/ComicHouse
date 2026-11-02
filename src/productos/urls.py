from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EditorialViewSet,
    AuthorViewSet,
    GeneroViewSet,
    ComicViewSet,
    PortadaViewSet,
    ClienteViewSet,
    ListaDeseosViewSet,
    PedidoViewSet,
    DetallePedidoViewSet,
    ResenaViewSet,
)

router = DefaultRouter()

router.register(r'editoriales', EditorialViewSet)
router.register(r'autores', AuthorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'comics', ComicViewSet)
router.register(r'portadas', PortadaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'listas-deseos', ListaDeseosViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]