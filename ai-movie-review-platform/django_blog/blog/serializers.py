"""DRF Serializers for CineAI blog API."""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    stars  = serializers.CharField(source='stars', read_only=True)

    class Meta:
        model  = Post
        fields = [
            'id', 'title', 'movie_title', 'content',
            'author', 'rating', 'stars', 'sentiment',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']
