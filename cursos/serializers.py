from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Horario, Carrera, Curso


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['hora_inicio', 'hora_fin']


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['nombre', 'total_cursos', 'tipo']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'creditos',
                  'horario', 'carrera', 'catedratico']
