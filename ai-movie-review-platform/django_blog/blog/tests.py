"""Tests for the CineAI blog app."""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Great Inception Review',
            movie_title='Inception',
            content='This movie blew my mind completely.',
            author=self.user,
            rating=5,
            sentiment='positive'
        )

    def test_post_str(self):
        self.assertIn('Great Inception Review', str(self.post))

    def test_stars_method(self):
        self.assertEqual(self.post.stars(), '★★★★★')

    def test_stars_partial(self):
        self.post.rating = 3
        self.assertEqual(self.post.stars(), '★★★☆☆')


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Review', movie_title='Test Movie',
            content='A great test movie review.', author=self.user,
            rating=4, sentiment='positive'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Review')

    def test_create_post_requires_login(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_create_post_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Review', 'movie_title': 'New Movie',
            'content': 'This is a new review content that is long enough.',
            'rating': 5, 'sentiment': 'positive'
        })
        self.assertEqual(Post.objects.count(), 2)

    def test_delete_post_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('delete_post', args=[self.post.pk]))
        self.assertEqual(Post.objects.count(), 0)
