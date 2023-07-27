from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def ver_usuarios(request):
    contexto =  {
        # No mostrar al staff o los superusuarios
        'usuarios': User.objects.filter(is_staff=False, is_superuser=False)
    }
    return render(request, 'usuarios/ver.html', contexto)