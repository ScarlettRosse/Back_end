from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    clases_impartidas = models.ManyToManyField('Clase', related_name='profesores')