"""DRF API views for CineAI blog."""

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/posts/  → List all posts
    POST /api/posts/  → Create a post (auth required)
    """
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/posts/<id>/  → Retrieve a post
    PUT    /api/posts/<id>/  → Update a post (auth required)
    DELETE /api/posts/<id>/  → Delete a post (auth required)
    """
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
