from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistro
from .models import ListaDeseos
from tienda.models import Producto

# Create your views here.
def ver_usuarios(request):
    contexto =  {
        'usuario_activo': request.user,
        # No mostrar al staff o los superusuarios
        'usuarios': User.objects.filter(is_staff=False, is_superuser=False)
    }
    return render(request, 'usuarios/ver.html', contexto)

def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            uname = request.POST['username']
            messages.success(request, f"Usuario {uname} creado con exito")
            return redirect('usuarios:ver-usuarios')

    contexto = {
        'formulario': FormularioRegistro(),
        'usuario_activo': request.user
    }
    return render(request, 'usuarios/registro.html', contexto)

@login_required()
def post_login(request):
    contexto = {'usuario_activo': request.user}
    return render(request, 'usuarios/post-login.html', contexto)

@login_required()
def lista_deseos(request):
    if request.method == 'POST':
        accion = request.POST['accion']

        if accion == 'agregar':
            pk_producto = int(request.POST['producto'])
            producto_elegido = get_object_or_404(Producto, pk=pk_producto)
            if request.user.is_authenticated:
                entrada_lista = ListaDeseos(usuario=request.user, producto=producto_elegido)
                entrada_lista.save()
                return redirect('usuarios:lista-deseos')

        elif accion == 'quitar':
            pk_objeto = int(request.POST['objeto'])
            if request.user.is_authenticated:
                objeto_elegido = ListaDeseos.objects.get(pk=pk_objeto)
                objeto_elegido.delete()

    contexto = {
        'usuario_activo': request.user,
        'lista_de_deseos': ListaDeseos.objects.filter(usuario=request.user)
    }
    return render(request, 'usuarios/lista_deseos.html', contexto)


def usuario_logout(request):
    logout(request)
    return redirect('landing:main-page')