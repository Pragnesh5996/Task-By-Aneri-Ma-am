from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import status

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response({"status":True, "message":"Fetch data successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def put(self,request,*args,**kwargs):
        user_data = ''
        try:
            user_data = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({"status":False, "error":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user_data, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Update data successfully", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "error":"Some Fields Are Missing", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,*args,**kwargs):
        user_data = ''
        try:
            user_data = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({"status":False, "error":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user_data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Partial Update data successfully", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "error":"Some Fields Are Missing", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,*args,**kwargs):
        user_data = ''
        try:
            user_data = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({"status":False, "error":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_data.delete()
        return Response({"status":True, "message":"User data deleted successfully"}, status=status.HTTP_200_OK)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer