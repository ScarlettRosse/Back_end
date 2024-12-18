from django.db import models
from Clase.models import Clase
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clases_inscritas = models.ForeignKey(Clase, on_delete=models.CASCADE )
