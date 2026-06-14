"""Views for CineAI blog – CRUD + Authentication."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Post
from .forms import PostForm, RegisterForm


# ── Public Views ─────────────────────────────────────────────────────────────

def home(request):
    posts = Post.objects.all()[:6]
    return render(request, 'blog/home.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# ── Auth Views ────────────────────────────────────────────────────────────────

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Account created.')
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# ── CRUD Views ────────────────────────────────────────────────────────────────

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Review posted successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form, 'action': 'Create'})


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only edit your own reviews.')
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create_post.html', {'form': form, 'action': 'Update', 'post': post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only delete your own reviews.')
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Review deleted.')
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})
