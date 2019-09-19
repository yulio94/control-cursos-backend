from django.db import models


class Catedratico(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    profesion = models.CharField(max_length=80)
    correo = models.EmailField()
    dpi = models.CharField(max_length=13)
