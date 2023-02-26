from django.urls import path
from Post.views import PostPublicList, PostView

urlpatterns = [
    path("post/", PostView.as_view(), name="user_post"),
    path("post/<int:pk>", PostView.as_view(), name="user_post_update"),
    path("PublicPost/", PostPublicList.as_view(), name="PublicPost")
]