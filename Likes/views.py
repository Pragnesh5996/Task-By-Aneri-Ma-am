from Post.models import Post as P
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Likes.models import Like
from Likes.serializers import LikeSerializer

# Create your views here.
class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.data["post"] = request.query_params.get("post_id")
        request.data["owner"] = request.user.id

        serializer = ''
        try:
            serializer = Like.objects.get(post=request.query_params.get("post_id"), owner=request.user.id)
        except Like.DoesNotExist:
            serializer = ''
        
        if serializer == '':
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                return Response({"status":True, "message":"you liked the post by id %s"%(request.query_params.get("post_id")), "data":serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status":False, "message":"you liked the post by id %s is not submiited"%(request.query_params.get("post_id"))}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":False, "message":"you already liked the post by id %s"%(request.query_params.get("post_id"))}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, format=None):
        post_likes = ''
        total_like = 0
        if request.query_params.get("post_id") != '' and request.query_params.get("post_id") is not None:
            post_likes = Like.objects.all().filter(post=request.query_params.get("post_id"))
        else:
            post_likes = Like.objects.all().filter(id=id, owner=request.user.id)

        if len(post_likes) > 0:
            serializer = LikeSerializer(post_likes, many=True)
            return Response({"status":True, "message":"Fetch Likes", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":False, "error":"Couldn't Fetch Likes", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        request.data["post"] = request.query_params.get("post_id")
        request.data["owner"] = request.user.id
        like_data = ''
        
        try:
            like_data = Like.objects.get(id=id, post=request.query_params.get("post_id"), owner=request.user.id)
        except Like.DoesNotExist:
            return Response({"status":False, "error":"Like Detail Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LikeSerializer(like_data, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"status":True, "message":"Update like", "data":serializer.data}, status=status.HTTP_200_OK) 
        else:
            return Response({"status":False, "error":"Couln't Update Like", "error_message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        like_data = ''
        try:
            like_data = Like.objects.get(id=id)
        except Like.DoesNotExist:
            return Response({"status":False, "error":"Like Detail Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        like_data.delete()
        return Response({"status":True, "message":"Unlike Successfully"}, status=status.HTTP_200_OK)