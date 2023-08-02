from typing import Any, Dict
from django.shortcuts import render
from .models import Producto
from django.views import generic

# Create your views here.
def main(request):
    contexto = {
        'usuario_activo': request.user,
        'productos': Producto.objects.order_by("-fecha_publicacion")[:6]
    }
    return render(request, 'tienda/index.html', contexto)

class VerProducto(generic.DetailView):
    model = Producto
    template_name = 'tienda/ver_producto.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['usuario_activo'] = self.request.user
        return contexto