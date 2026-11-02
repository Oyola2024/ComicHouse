from django.shortcuts import render
from .models import Comic, Autor, Editorial, Genero, Pedido, Portada, Cliente, ListaDeseos, DetallePedido, Resena
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 
from drf_spectacular.utils import extend_schema, OpenApiResponse


from .serializers import (
    RegistroSerializer,
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
    ResenaListSerializer,
    ComicAuthorSerializer,
)


def home(request):
    return render(request, 'home.html')

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.none()
    serializer_class = RegistroSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all().order_by('nombre')
    serializer_class = EditorialSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'direccion', 'telefono']

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'apellido']

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('nombre')
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all().select_related('autor', 'editorial', 'genero').order_by('titulo')
    serializer_class = ComicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'titulo': ['icontains'],
        'autor__nombre': ['icontains'],
        'editorial__nombre': ['icontains'],
        'genero__nombre': ['icontains'],
        'precio': ['exact','gt','lt','gte', 'lte'],
        'stock': ['exact','gt','lt','gte', 'lte'],
    }

    search_fields = ['titulo', 'autor__nombre', 'editorial__nombre', 'genero__nombre']

    def get_serializer_class(self):
        if self.action == 'list':
            return ComicAuthorSerializer
        return ComicSerializer

    @extend_schema(
        summary="Listar cómics sin stock",
        description="Devuelve los cómics cuyo stock es 0.",
        responses=ComicSerializer(many=True),
    )
    @action(detail=False, methods=['get'])
    def sin_stock(self, request):
        comics = self.get_queryset().filter(stock=0)
        serializer = self.get_serializer(comics, many=True)
        return Response(serializer.data)

class PortadaViewSet(viewsets.ModelViewSet):
    queryset = Portada.objects.all().select_related('comic').order_by('comic__titulo')
    serializer_class = PortadaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comic__titulo']

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'apellido', 'email', 'telefono']

class ListaDeseosViewSet(viewsets.ModelViewSet):
    queryset = ListaDeseos.objects.all().select_related('cliente').prefetch_related('comics').order_by('cliente__nombre')
    serializer_class = ListaDeseosSerializer
    permission_classes = [IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        summary="Cancelar un pedido",
        description="Cambia el estado del pedido a 'cancelado'. No necesita body.",
        request=None,
        responses={
            200: PedidoSerializer,
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
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().select_related('comic', 'cliente').order_by('-fecha_resena')
    serializer_class = ResenaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Datos anidados (comic y cliente completos) solo en el list
    def get_serializer_class(self):
        if self.action == 'list':
            return ResenaListSerializer
        return ResenaSerializer
