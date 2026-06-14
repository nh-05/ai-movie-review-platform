"""Blog models for CineAI movie review platform."""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


SENTIMENT_CHOICES = [
    ('positive', 'Positive'),
    ('negative', 'Negative'),
    ('neutral',  'Neutral'),
]

RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]


class Post(models.Model):
    """A movie review blog post."""
    title       = models.CharField(max_length=200)
    movie_title = models.CharField(max_length=200, default='')
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    rating      = models.IntegerField(choices=RATING_CHOICES, default=5)
    sentiment   = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, default='neutral')
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} — by {self.author.username}'

    def stars(self):
        return '★' * self.rating + '☆' * (5 - self.rating)
