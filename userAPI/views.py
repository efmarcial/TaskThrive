from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import uuid
import hashlib

# API Key ID: eTD6YPlMSGeWjqYFCQtQGg
# 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


class TestView(APIView):
    def get(self, request, format=None):
        print("API was called")
        return Response("You made it", status=201)
    

class UserView(APIView):
    
    def post(self, request, format=None):
        print("Creating a user")
        
        user_data = request.data
        print(user_data)
        
        
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid(raise_exception=False):
            
            user_serializer.save()
            print("User Created & Saved")
            
            salt = uuid.uuid4().hex
            hash_object = hashlib.sha256(salt.encode() + str(user_serializer.data['id']).encode())
            
            token = hash_object.hexdigest() + ':' + salt
            
            message = Mail(
                from_email="taskthrive@mail.com",
                to_emails = user_data["email"],
                subject="Confirm email address", 
                html_content=f"\
                    Hi {user_data['first_name']},\
                    <br><br>Thank you for signing up. To confirm your email, please click <a href='http://127.0.0.1:8000/api/v1.0/user/verify-user/{token}'>Here</a>"
            )
            
            try:
                
                sg = SendGridAPIClient("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")
                response = sg.send(message)
                
                print(response)
                
                return Response( user_serializer.data, status=200)
            
            except Exception as e:
                print(e)
            
            
        
        return Response({"msg":"ERR"}, status=400)

class UserVerificationView(APIView):
    
    def get(self, request, pk, format=None):
        print(f'Verifing User')
    
     
class UserLoginView(APIView):
    
    # Convert a user token into user data
    def get(self, request, format=None):
        
        if request.user.is_authenticated == False or request.user.is_active == False:
            return Response("Invalid Credentials", status=403)
        
        user = UserSerializer(request.user)
        print(user.data)
        
        return Response(user.data, status=200)
    
    def post(self, request, format=None):
        
        print(request.data)
       
        try:
            user_obj = User.objects.filter(email = request.data['username'].lower()).first() or User.objects.filter(username=request.data["username"].lower()).first()
            if user_obj is not None:
                credentials = {
                    'username': user_obj.username,
                    'password' : request.data["password"]
                }
                user = authenticate(**credentials)
                
                if user and user.is_active:
                    user_serializer = UserSerializer(user)
                    return Response(user_serializer.data, status=200)
            else:
                print("Invalid Credentials!")
                content = {
                    "error" : "Invalid Credentials!"
                }
                return Response(content, status=403)
        except Exception as e:
            
            print(f'Error in backend: {e}')
            
            content = {
                    "error" : "Invalid Credentials!"
                }
            return Response(content, status=403)
            
       
        
        return Response("Invalid Credentail", status=403)