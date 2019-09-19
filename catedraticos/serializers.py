from .models import Catedratico
from rest_framework import serializers


class CatedraticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catedratico
        fields = ['nombre', 'apellido', 'profesion', 'correo', 'dpi']
