from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('ver/', views.ver_usuarios, name='ver-usuarios'),
    path('registro/', views.registro, name='registro'),
    path('post-login/', views.post_login, name='post-login'),
    path('lista-deseos/', views.lista_deseos, name='lista-deseos'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),
    path('logout/', views.usuario_logout, name='logout')
]