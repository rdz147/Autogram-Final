# auto/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm, CommentForm

def index_view(request):
    return render(request, 'auto/index.html')

class FeedView(ListView):
    model = Post
    template_name = 'auto/feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'auto/post_detail.html'

@login_required
def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'auto/add_post.html', {'form': form})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'auto/post_detail.html', {'form': form, 'post': post})

@login_required
def feed_view(request):
    posts = Post.objects.all()
    return render(request, 'auto/feed.html', {'posts': posts})