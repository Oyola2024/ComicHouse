from django.contrib import admin

from .models import Editorial, Genero, Autor, Comic, Portada, Cliente, ListaDeseos, Pedido, DetallePedido, Resena

admin.site.site_header = "Comic House Admin"
admin.site.site_title = "Comic House Admin Portal"
admin.site.index_title = "Panel de control de la libreria"


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')
    ordering = ('nombre',)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'biografia')
    search_fields = ('nombre', 'apellido', 'biografia')
    ordering = ('apellido', 'nombre')


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'genero', 'fecha_publicacion', 'precio', 'stock')
    search_fields = ('titulo', 'autor__nombre', 'editorial__nombre', 'genero__nombre')
    list_filter = ('autor', 'editorial', 'genero', 'fecha_publicacion')
    ordering = ('titulo',)


@admin.register(Portada)
class PortadaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'imagen', 'descripcion')
    search_fields = ('comic__titulo', 'descripcion')
    list_filter = ('comic',)
    ordering = ('comic__titulo',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'user')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')
    ordering = ('apellido', 'nombre')


@admin.register(ListaDeseos)
class ListaDeseosAdmin(admin.ModelAdmin):
    list_display = ('cliente',)
    search_fields = ('cliente__nombre', 'cliente__apellido')
    list_filter = ('cliente',)
    filter_horizontal = ('comics',)  # selector cómodo para elegir muchos comics


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'estado', 'total')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    list_filter = ('estado', 'fecha_pedido')
    ordering = ('-fecha_pedido',)


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'comic', 'cantidad', 'precio_unitario')
    search_fields = ('pedido__id', 'comic__titulo')
    list_filter = ('comic',)
    ordering = ('-pedido__id',)


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'cliente', 'calificacion', 'comentario', 'fecha_resena')
    search_fields = ('comic__titulo', 'cliente__nombre', 'cliente__apellido', 'comentario')
    list_filter = ('calificacion', 'comic')
    ordering = ('-fecha_resena',)
