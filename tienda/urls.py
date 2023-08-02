from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:pk>/', views.VerProducto.as_view(), name='ver-producto'),
]
