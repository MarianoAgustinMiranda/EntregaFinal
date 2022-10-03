from enum import unique
from django.db import models

class Propiedad(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    numeroprop = models.IntegerField(unique=True, null= True)

    def __str__(self):
        return f'Propiedad: {self.nombre}, NumeroProp: {self.numeroprop}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Inmobiliario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    