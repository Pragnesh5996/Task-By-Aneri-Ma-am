from Post.models import Post
from Likes.models import Like
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(method_name="get_count_likes") 
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'public', 'owner', 'likes']

    def get_count_likes(self, obj):
        return obj.postlikes.count()
