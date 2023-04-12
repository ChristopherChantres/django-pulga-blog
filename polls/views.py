from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {'posts':posts})


def create(request):
  if request.method == 'POST':
    post_title = request.POST['post_title']
    post_author = request.POST['post_author']
    post_content = request.POST['post_content']

    if Post.objects.filter(title=post_title).exists():
      messages.info(request, 'Post title alredy used')
      return redirect('create')
    else:
      new_post = Post.objects.create(title=post_title, author=post_author, content=post_content, created_at=timezone.now(), updated_at=timezone.now())
      new_post.save()
      return redirect('home')
  else:
    return render(request, 'create.html')


def edit(request):
  return render(request, 'edit.html')


def post_detail(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'post_detail.html', {'post': post})