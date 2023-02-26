from django.urls import path
from User import views as user_view
from rest_framework.authtoken import views

urlpatterns = [
    path('Login/', views.obtain_auth_token, name="Login"),
    path('Detail/', user_view.UserDetailAPI.as_view(), name="user_detail"),
    path('Register/', user_view.RegisterUserAPIView.as_view(), name="Register"),
]