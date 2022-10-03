from django.urls import path
from Inmobiliaria.views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('propiedades/', propiedad, name="Propiedades"),
    path('propiedadFormulario/', propiedadFormulario, name='PropiedadFormulario'),
    path('clientes/', clientes, name="Clientes"),
    path('inmobiliarios/', inmobiliarios, name="Inmobiliarios"),
    path('buscarNumeroprop/', buscarNumeroprop, name='BuscarNumeroProp'),
    path('buscarNumeropropPost/', buscarNumeropropPost, name='BuscarNumeroPropPost'),
    path('editarPropiedad/<int:numeroprop>', editarPropiedad, name='EditarPropiedad'),
    path('eliminarPropiedad/<int:numeroprop>', eliminarPropiedad,name='EliminarPropiedad'),
]
