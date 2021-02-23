from django.shortcuts import render,get_object_or_404
from blog.models import BlogPost


def index(request):
    blog_posts = BlogPost.objects.filter().order_by('-date')[0:3]
    return render(request, 'index.html', {
        'blog_posts': blog_posts
    })


def photos(request):
    return render(request, 'photos.html')
