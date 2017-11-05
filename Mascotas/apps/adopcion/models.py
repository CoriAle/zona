from django.db import models

# Create your models here.

class Persona(models.Model):
    """docstring for Persona."""
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=10)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razon = models.TextField()
