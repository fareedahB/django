from django.shortcuts import render
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    context = {"gender":"Female", "posts" : posts}
    return render(request, 'blog/list.html', context)

