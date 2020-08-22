from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from posts import views

router = DefaultRouter()
router.register(r'writeposts', views.WritePostsViewSet)
router.register(r'clickposts', views.ClickPostsViewSet)
router.register(r'artposts', views.ArtPostsViewSet)

urlpatterns = [
    # path('WritePosts/', views.WritePostsList.as_view()),
    # path('WritePosts/<int:pk>/', views.WritePostsDetail.as_view()),
    # path('ClickPosts/', views.ClickPostsList.as_view()),
    # path('ClickPosts/<int:pk>/', views.ClickPostsDetail.as_view()),
    # path('ArtPosts/', views.ArtPostsList.as_view()),
    # path('ArtPosts/<int:pk>/', views.ArtPostsDetail.as_view()),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)