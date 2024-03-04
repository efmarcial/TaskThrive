from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, format=None):
        print("API was called")
        return Response("You made it", status=201)