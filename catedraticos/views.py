from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Catedratico
from .serializers import CatedraticoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def catedratico_list_view(request):
    """
        List all catedraticos, or create a new.
    """
    if request.method == 'GET':
        catedratico = Catedratico.objects.all()
        serializer = CatedraticoSerializer(catedratico, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CatedraticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def catedratico_detail_view(request, pk):

    try:
        catedratico = Catedratico.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CatedraticoSerializer(catedratico)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CatedraticoSerializer(catedratico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        catedratico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
