from django import forms

class PropiedadFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(max_length=120)

class BusquedaNumeropropFormulario(forms.Form):
    numeroprop = forms.IntegerField()


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class InmobiliarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()