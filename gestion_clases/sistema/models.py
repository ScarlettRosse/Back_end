from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.TimeField()
    descripcion = models.TextField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clases_inscritas = models.ManyToManyField('Clase', related_name='estudiantes')

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    clases_impartidas = models.ManyToManyField('Clase', related_name='profesores')