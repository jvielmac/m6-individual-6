from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField(max_length=300)
    precio = models.IntegerField()
    tipo_producto = models.CharField(max_length=20)
    autor =  models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo