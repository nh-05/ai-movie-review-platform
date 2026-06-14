"""DRF API URL patterns."""

from django.urls import path
from .api_views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/',        PostListCreateAPIView.as_view(),          name='api_post_list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='api_post_detail'),
]
