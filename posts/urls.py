from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    path('WritePosts/', views.WritePostsList.as_view()),
    path('WritePosts/<int:pk>/', views.WritePostsDetail.as_view()),
    path('ClickPosts/', views.ClickPostsList.as_view()),
    path('ClickPosts/<int:pk>/', views.ClickPostsDetail.as_view()),
    path('ArtPosts/', views.ArtPostsList.as_view()),
    path('ArtPosts/<int:pk>/', views.ArtPostsDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)