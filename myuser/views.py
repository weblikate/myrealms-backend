from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, ProfileSerializer


class SignupView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JWTAuthentication,)
    serializer_class=ProfileSerializer


