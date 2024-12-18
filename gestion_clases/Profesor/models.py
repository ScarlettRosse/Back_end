from django.db import models
from Clase.models import Clase
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    clases_impartidas = models.ForeignKey(Clase, on_delete=models.CASCADE )