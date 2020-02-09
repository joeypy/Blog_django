from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context= {'posts': posts})

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', context= {'post': post})