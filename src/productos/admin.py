from django.contrib import admin

from .models import Editorial, Genero, Autor, Comic, Portada, Cliente, Pedido, DetallePedido, Resena    

admin.site_header = "Comic House Admin"
admin.site_title = "Comic House Admin Portal"
admin.site.index_title = "Panel de control de la libreria"

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'biografia')
    search_fields = ('nombre', 'apellido', 'biografia')

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'genero', 'fecha_publicacion', 'precio', 'stock')
    search_fields = ('titulo', 'autor__nombre', 'editorial__nombre', 'genero__nombre')
    list_filter = ('autor', 'editorial', 'genero')

@admin.register(Portada)
class PortadaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'imagen', 'descripcion')
    search_fields = ('comic__titulo', 'descripcion')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_pedido', 'total')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'fecha_pedido', 'total')

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'comic', 'cantidad', 'precio_unitario')
    search_fields = ('pedido__id', 'comic__titulo', 'cantidad', 'precio_unitario')

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'cliente', 'calificacion', 'comentario')
    search_fields = ('comic__titulo', 'cliente__nombre', 'cliente__apellido', 'calificacion', 'comentario')

