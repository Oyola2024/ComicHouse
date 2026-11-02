from django.shortcuts import render
from .models import Comic, Autor, Editorial, Genero, Pedido, Portada, Cliente, ListaDeseos, DetallePedido, Resena
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    ComicSerializer,
    AutorSerializer,
    EditorialSerializer,
    GeneroSerializer,
    PortadaSerializer,
    ClienteSerializer,
    ListaDeseosSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
    ResenaSerializer,
)
# Create your views here.


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all().order_by('nombre')
    serializer_class = EditorialSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('nombre')
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all().select_related('autor', 'editorial', 'genero').order_by('titulo')
    serializer_class = ComicSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="Listar cómics sin stock",
        description="Devuelve una lista de cómics que no tienen stock disponible.",
        responses={
            200: ComicSerializer,
            400: OpenApiResponse(description="Solicitud inválida"),
        }
    )

    @action(detail=True, methods=['get'])
    def sin_stock(self, request, pk=None):
        comic = self.get.queryset().filter(stock=0)
        serializer = self.get_serializer(comic, many=True)
        return Response(serializer.data)
        
class PortadaViewSet(viewsets.ModelViewSet):
    queryset = Portada.objects.all().select_related('comic').order_by('comic__titulo')
    serializer_class = PortadaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ListaDeseosViewSet(viewsets.ModelViewSet):
    queryset = ListaDeseos.objects.all().select_related('cliente').prefetch_related('comics').order_by('cliente__nombre')
    serializer_class = ListaDeseosSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="Cancelar un pedido",
        description="Permite cancelar un pedido existente.",
        responses={
            200: PedidoSerializer,
            400: OpenApiResponse(description="Solicitud inválida"),
            404: OpenApiResponse(description="Pedido no encontrado"),
        }
    )

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        pedido = self.get_object()
        pedido.estado = 'cancelado'
        pedido.save()
        serializer = self.get_serializer(pedido)
        return Response(serializer.data)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all().select_related('pedido', 'comic')
    serializer_class = DetallePedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().select_related('comic', 'cliente')
    serializer_class = ResenaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

