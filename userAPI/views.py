from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import UserSerializer

class TestView(APIView):
    def get(self, request, format=None):
        print("API was called")
        return Response("You made it", status=201)
    

class UserView(APIView):
    
    def post(self, request, format=None):
        print("Creating a user")
        
        user_data = request.data
        print(request.data)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=False):
            
            user_serializer.save()
            print("User Created & Saved")
            
            return Response({"user" : user_serializer.data}, status=200)
        
        return Response({"msg":"ERR"}, status=400)