from django.db import models

# Modelos app catedratico
from catedraticos import models as models_catedratico


class Horario(models.Model):
    hora_inicio = models.DateField()
    hora_fin = models.DateField()


class Carrera(models.Model):
    nombre = models.CharField(max_length=60)
    total_cursos = models.IntegerField()
    tipo = models.CharField(max_length=50)


class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=140)
    creditos = models.IntegerField(default=1)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(
        models_catedratico.Catedratico, on_delete=models.CASCADE)
