from django.urls import path
from Likes.views import LikeView

urlpatterns = [ 
    path("like/", LikeView.as_view(), name="postLike"),
    path("like/<int:id>", LikeView.as_view(), name="updatelike"),
]