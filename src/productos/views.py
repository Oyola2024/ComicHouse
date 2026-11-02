from django.shortcuts import render
from .models import Comic, Autor, Editorial, Genero, Pedido, Portada, Cliente, ListaDeseos, DetallePedido, Resena
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

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

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('nombre')
    serializer_class = GeneroSerializer

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all().select_related('autor', 'editorial', 'genero').order_by('titulo')
    serializer_class = ComicSerializer

class PortadaViewSet(viewsets.ModelViewSet):
    queryset = Portada.objects.all().select_related('comic').order_by('comic__titulo')
    serializer_class = PortadaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer

class ListaDeseosViewSet(viewsets.ModelViewSet):
    queryset = ListaDeseos.objects.all().select_related('cliente').prefetch_related('comics').order_by('cliente__nombre')
    serializer_class = ListaDeseosSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().select_related('cliente').prefetch_related('detalles')
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all().select_related('pedido', 'comic')
    serializer_class = DetallePedidoSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().select_related('comic', 'cliente')
    serializer_class = ResenaSerializer

