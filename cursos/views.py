from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carrera, Curso, Horario
from .serializers import CarreraSerializer, CursoSerializer, HorarioSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def carrera_list_view(request):
    """
        List all carreras, or create a new.
    """
    if request.method == 'GET':
        carrera = Carrera.objects.all()
        serializer = CarreraSerializer(carrera, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarreraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def carrera_detail_view(request, pk):

    try:
        carrera = Carrera.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarreraSerializer(carrera)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CarreraSerializer(carrera, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        carrera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def curso_list_view(request):
    """
        List all carreras, or create a new.
    """
    if request.method == 'GET':
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def curso_detail_view(request, pk):

    try:
        curso = Curso.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarreraSerializer(curso)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CarreraSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def horario_list_view(request):
    """
        List all carreras, or create a new.
    """
    if request.method == 'GET':
        horario = Horario.objects.all()
        serializer = CarreraSerializer(horario, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarreraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def horario_detail_view(request, pk):

    try:
        horario = Horario.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HorarioSerializer(horario)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CarreraSerializer(horario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        horario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
