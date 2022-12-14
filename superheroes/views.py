from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Superhero
from .serializers import SuperheroSerializer


# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def superheroes_list(request):
    if request.method == 'GET':
        superheroes = Superhero.objects.all()
        serializer = SuperheroSerializer(superheroes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SuperheroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def superhero_detail(request, id):
    try:
        superhero = Superhero.objects.get(id=id)
    except Superhero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuperheroSerializer(superhero)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SuperheroSerializer(superhero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        superhero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
