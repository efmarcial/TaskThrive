from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.models import Service
from main_app.serializer import ServiceSerializer

@api_view(['GET', 'POST'])
def service_list(request, format=None):
    """
    List all code snippets, or create a new service
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk, format=None):
    """
    Retrive, update or delete a code snippet.
    """
    try: 
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)