from django.shortcuts import render

# Create your views here.
def mainpage(request):
    contexto = {'usuario_activo': request.user}
    return render(request, 'landing/index.html', contexto)

def politica_privacidad(request):
    contexto = {
        'usuario_activo': request.user,
        'titulo': 'Política de Privacidad',
        'secciones': range(1, 4)
    }
    return render(request, 'landing/placeholder.html', contexto)

def terminos_y_condiciones(request):
    contexto = {
        'usuario_activo': request.user,
        'titulo': 'Términos y condiciones',
        'secciones': range(1, 4)
    }
    return render(request, 'landing/placeholder.html', contexto)

def mapa_sitio(request):
    contexto = {'usuario_activo': request.user}
    return render(request, 'landing/mapa.html', contexto)