from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny

import json

from authentication.serializer import UserSerializer


class UserSignupView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.exists():
            return Response({"error": "Only one librarian can be created."}, status=status.HTTP_400_BAD_REQUEST)

        
        user = User.objects.create_user(username=username, email=email, password=password)

       
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            "message": "User created successfully",
            "username": user.username,
            "email": user.email,
            "access_token": access_token,
            "refresh_token": str(refresh),
        }, status=status.HTTP_201_CREATED)



class LoginView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')  
        password = request.data.get('password')

        
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": str(refresh),
        }, status=status.HTTP_200_OK)
        
class AdminUserListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class AdminUserDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
