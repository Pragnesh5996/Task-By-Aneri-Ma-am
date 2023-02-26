from rest_framework import serializers
from Likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'likes', 'post', 'owner']