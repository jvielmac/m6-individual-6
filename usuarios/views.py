from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormularioRegistro

# Create your views here.
def ver_usuarios(request):
    contexto =  {
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
        else:
            print("Foemulario invalido")
            contexto = {
                'formulario': FormularioRegistro(),
                'mensaje': 'El formulario es invalido.',
                'tipo': 'alert-warning'
            }
            return render(request, 'usuarios/registro.html', contexto)
    else:
        contexto = {'formulario': FormularioRegistro()}
        return render(request, 'usuarios/registro.html', contexto)