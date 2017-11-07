from django.db import models
from apps.adopcion.models import Persona
# Create your models here.

class Vacuna(models.Model):
    """docstring for Vacuna."""
    nombre=models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    funcion= models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    """docstring forMascota."""
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    edad= models.IntegerField()
    fecha_rescate = models.DateField()
    imagen = models.ImageField(blank = True)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)
