from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('ver/', views.ver_usuarios, name='ver-usuarios')
]