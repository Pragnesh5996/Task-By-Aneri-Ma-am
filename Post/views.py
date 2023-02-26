from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from django.contrib.auth.models import User
from Post.models import Post as P
from rest_framework import status


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.data["owner"] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Post Created", "data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":False, "error":"Post Not Created", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        post_data = ''
        try:
            post_data = P.objects.get(id=pk, owner=request.user.id)
        except P.DoesNotExist:
            return Response({"status":False, "error":"Post Not Found"}, status=status.HTTP_404_NOT_FOUND)
        request.data["owner"] = request.user.id
        serializer = PostSerializer(post_data, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Post Updated", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "error":"Post Not Updated", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        post_data = ''
        try:
            post_data = P.objects.get(id=pk, owner=request.user.id)
        except P.DoesNotExist:
            return Response({"status":False, "error":"Post Not Found"}, status=status.HTTP_404_NOT_FOUND)
        request.data["owner"] = request.user.id
        serializer = PostSerializer(post_data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Post Partial Updated", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "error":"Post Not Partial Updated", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        post_data = ''
        try:
            post_data = P.objects.get(id=pk, owner=request.user.id)
        except P.DoesNotExist:
            return Response({"status":False, "error":"Post Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        post_data.delete()
        return Response({"status":True, "message":"Post Deleted"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None, format=None):
        posts = ''
        if pk is not None:
            posts = P.objects.filter(id=pk, owner=request.user.id)
        else:
            posts = P.objects.all().filter(owner=request.user.id)
        if len(posts) > 0:
            serializer = PostSerializer(posts, many=True)
            return Response({"status":True, "message":"Post Fetched", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "Error":"No Post Found."}, status=status.HTTP_404_NOT_FOUND)

class PostPublicList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        posts = P.objects.all().filter(public=True)
        if len(posts) > 0:
            serializer = PostSerializer(posts, many=True)
            return Response({"status":True, "message":"Post Fetched", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "Error":"No Post Found."}, status=status.HTTP_404_NOT_FOUND)