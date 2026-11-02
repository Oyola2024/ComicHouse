from rest_framework import serializers
from .models import  Editorial, Genero, Autor, Comic, Portada, Cliente, ListaDeseos, Pedido, DetallePedido , Resena

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = [
            'id',
            'nombre',
            'direccion',
            'telefono',
        ]

        read_only_fields = ['id']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = [
            'id',
            'nombre',
            'descripcion',
        ]

        read_only_fields = ['id']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = [
            'id',
            'nombre',
            'apellido',
            'biografia',
        ]

        read_only_fields = ['id']

    

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = [
            'id',
            'titulo',
            'autor',
            'editorial',
            'genero',
            'fecha_publicacion',
            'precio',
            'stock',
        ]

        read_only_fields = ['id']

class ComicAuthorSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)

    class Meta:
        model = Comic
        fields = [
            'id',
            'titulo',
            'autor',
            'editorial',
            'genero',
            'fecha_publicacion',
            'precio',
            'stock',
        ]

        read_only_fields = ['id']


class PortadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portada
        fields = [
            'id',
            'comic',
            'imagen',
            'descripcion',
        ]

        read_only_fields = ['id']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'apellido',
            'email',
            'telefono',
        ]

        read_only_fields = ['id']

class ListaDeseosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeseos
        fields = [
            'id',
            'cliente',
            'comics',
        ]

        read_only_fields = ['id']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'id',
            'cliente',
            'fecha_pedido',
            'total',
        ]

        read_only_fields = ['id']


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = [
            'id',
            'pedido',
            'comic',
            'cantidad',
            'precio_unitario',
        ]
        read_only_fields = ['id']

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = [
            'id',
            'comic',
            'cliente',
            'calificacion',
            'comentario',
        ]

        read_only_fields = ['id']


