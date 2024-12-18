from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.TimeField()
    descripcion = models.TextField()