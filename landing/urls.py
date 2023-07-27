from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.mainpage, name='main-page'),
    path('privacidad/', views.politica_privacidad, name='politica-privacidad'),
    path('terminos-y-condiciones/', views.terminos_y_condiciones, name='terminos-y-condiciones'),
    path('mapa/', views.mapa_sitio, name='mapa-sitio')
]