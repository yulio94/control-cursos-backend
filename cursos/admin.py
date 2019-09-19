from django.contrib import admin
from .models import Carrera, Curso, Horario


# Register your models here.
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Horario)
