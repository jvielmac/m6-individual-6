from django.db import models
from django.contrib.auth.models import User
from tienda.models import Producto

# Create your models here.
class ListaDeseos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)