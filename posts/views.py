from django.shortcuts import render
from rest_framework import generics, viewsets
from posts.models import *
from posts.serializers import *
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,AllowAny
# Create your views here.

# class WritePostsList(generics.ListCreateAPIView):
#     queryset = WritePosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = WritePostsSerializer


# class WritePostsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = WritePosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = WritePostsSerializer


# class ClickPostsList(generics.ListCreateAPIView):
#     queryset = ClickPosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = ClickPostsSerializer


# class ClickPostsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ClickPosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = ClickPostsSerializer


# class ArtPostsList(generics.ListCreateAPIView):
#     queryset = ArtPosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = ArtPostsSerializer


# class ArtPostsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ArtPosts.objects.all()
#     permission_classes=(IsAuthenticated,)
#     serializer_class = ArtPostsSerializer


class WritePostsViewSet(viewsets.ModelViewSet):
    queryset = WritePosts.objects.all()
    permission_classes= [IsAuthenticated,]
    serializer_class = WritePostsSerializer

class ClickPostsViewSet(viewsets.ModelViewSet):
    queryset = ClickPosts.objects.all()
    permission_classes= [IsAuthenticated,]
    serializer_class = ClickPostsSerializer

class ArtPostsViewSet(viewsets.ModelViewSet):
    queryset = ArtPosts.objects.all()
    permission_classes= [IsAuthenticated,]
    serializer_class = ArtPostsSerializer