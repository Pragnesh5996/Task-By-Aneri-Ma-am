from django.db import models
from django.contrib.auth.models import User
from Post.models import Post

# Create your models here.
class Like(models.Model):
    likes = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postlikes")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likebyuser")

    def __str__(self):
        return str(self.likes)