from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from pip._vendor.requests import post

from .models import BlogPost, Category, Comment
from .comment_form import CommentForm


def blog(request):
    blog_posts = BlogPost.objects.filter().order_by('-date')
    categories = Category.objects.all()
    context = {'blog_posts': blog_posts, 'categories': categories}
    return render(request, 'blog-home.html', context)


def blog_detail(request, category_slug, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    categories = Category.objects.all()
    comments = Comment.objects.filter(blog_post=blog_post).order_by('-date')

    if request.method == "POST":

        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment1 = Comment.objects.create(blog_post=blog_post, name=name, email=email, comment=comment)
            comment1.save()
            context = {
                'blog_post': blog_post,
                'categories': categories,
                'comments': comments,
                'comment_form': comment_form
            }
            return render(request, 'blog_post.html', context)

    else:
        comment_form = CommentForm()
    context = {
        'blog_post': blog_post,
        'categories': categories,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'blog_post.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blog_posts = category.blog_posts.all()
    context = {
        'category': category,
        'blog_posts': blog_posts
    }

    return render(request, 'blog_category_view.html', context)
