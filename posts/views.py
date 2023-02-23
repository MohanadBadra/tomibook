from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})

def posts(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts.html', {'posts':post})