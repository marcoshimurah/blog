from django.shortcuts import render

from .models import Post

def list_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)