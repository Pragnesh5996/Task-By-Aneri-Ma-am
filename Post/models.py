from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title