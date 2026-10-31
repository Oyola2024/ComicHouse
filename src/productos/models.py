from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Comic(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.titulo

class Portada(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='portadas/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Portada de {self.comic.titulo}"    


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ListaDeseos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comics = models.ManyToManyField(Comic, blank=True)

    def __str__(self):
        return f"Lista de deseos de {self.cliente.nombre} {self.cliente.apellido}"


class Pedido(models.Model):
    estado_choices = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comics = models.ManyToManyField(Comic, through='DetallePedido')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=estado_choices, default='pendiente')

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} {self.cliente.apellido} - Total: {self.total}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle del pedido {self.pedido.id} - Comic: {self.comic.titulo} - Cantidad: {self.cantidad}"

class Resena(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha_resena = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.cliente.nombre} {self.cliente.apellido} - Comic: {self.comic.titulo}"