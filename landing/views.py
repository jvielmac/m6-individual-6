from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'landing/index.html')

def politica_privacidad(request):
    contexto = {
        'titulo': 'Política de Privacidad',
        'secciones': range(1, 4)
    }
    return render(request, 'landing/placeholder.html', contexto)

def terminos_y_condiciones(request):
    contexto = {
        'titulo': 'Términos y condiciones',
        'secciones': range(1, 4)
    }
    return render(request, 'landing/placeholder.html', contexto)

def mapa_sitio(request):
    return render(request, 'landing/mapa.html')