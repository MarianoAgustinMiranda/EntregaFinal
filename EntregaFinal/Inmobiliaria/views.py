from email.mime import message
from django.shortcuts import render, redirect
from django.contrib import messages

from Inmobiliaria.forms import BusquedaNumeropropFormulario, PropiedadFormulario, ClienteFormulario
from Inmobiliaria.models import Propiedad, Cliente


def inicio(request):

    return render(request, 'Inmobiliaria/inicio.html')

def propiedad(request):
    propiedades = Propiedad.objects.all()

    contexto = {
        'propiedades' : propiedades
    }  

    return render(request, 'Inmobiliaria/propiedades.html', contexto)

def propiedadFormulario(request):

      if request.method == 'POST':

            miFormulario = PropiedadFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid: 

                  data = miFormulario.cleaned_data

                  propiedad1 = Propiedad(nombre=data.get['nombre'], numeroprop=data.get('numeroprop')) 

                  propiedad1.save()

                  return redirect("Inmobiliaria/inicio.html")

      propiedades = Propiedad.objects.all()

      contexto = {
            'form': PropiedadFormulario(),
            'propiedades': propiedades
      }

      return render(request, "Inmobiliaria/propiedadFormulario.html", contexto) 

def editarPropiedad(request, numeroprop):
      propiedad_editar = Propiedad.objects.get(numeroprop=numeroprop)

      if request.method == 'POST':

            miFormulario = PropiedadFormulario(request.POST)

            if miFormulario.is_valid():

                  data = miFormulario.cleaned_data

                  propiedad_editar.nombre = data.get('nombre')
                  propiedad_editar.numeroprop = data.get('numeroprop')

                  propiedad_editar.save()

                  return redirect ('Propiedades')
      contexto ={
            'form': PropiedadFormulario(
                  initial={
                        'nombre': propiedad_editar.nombre,
                        'numeroprop': propiedad_editar.numeroprop
                  }
            )
      }

      return render(request, 'PropiedadFormulario', contexto)
    
def eliminarPropiedad(request, numeroprop):
      propiedad_eliminar = Propiedad.objects.get(numeroprop=numeroprop)
      propiedad_eliminar.delete()

      messages.info(request, f'La propiedad {propiedad_eliminar} fue eliminada')

      return redirect('Propiedades')

def buscarNumeroprop(request):

      contexto = {
            'form': BusquedaNumeropropFormulario(),
      }

      return render(request, 'BuscarNumeroProp', contexto)

def buscarNumeropropPost(request):

      numeroprop = request.GET.get('numeroprop')

      propiedades = Propiedad.objects.filter(numeroprop__icontains=numeroprop)

      contexto ={
            'propiedades' : propiedades
      }

      return render(request, 'BuscarNumeroPropPost', contexto)

def clientes(request):

    return render(request, 'Inmobiliaria/clientes.html')

def clients(request):

      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid: 

                  informacion = miFormulario.cleaned_data
                  
                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  cliente.save()

                  return render(request, "Inmobiliaria/inicio.html")

      else: 

            miFormulario= ClienteFormulario() 

      return render(request, "Inmobiliaria/clientes.html", {"miFormulario":miFormulario})

def inmobiliarios(request):

    return render(request, 'Inmobiliaria/inmobiliarios.html')



