from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'movie_title', 'author', 'rating', 'sentiment', 'created_at']
    list_filter   = ['sentiment', 'rating', 'created_at']
    search_fields = ['title', 'movie_title', 'content', 'author__username']
