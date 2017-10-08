from django.db import models

# Create your models here.

class Persona(models.Model):
    """docstring for Persona."""
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=10)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    corrreo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)
