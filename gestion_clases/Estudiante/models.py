from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clases_inscritas = models.ManyToManyField('Clase', related_name='estudiantes')

