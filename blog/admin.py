from django.contrib import admin
from .models import Category, BlogPost, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date')
    search_fields = ('title', 'author', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date', 'blog_post', 'active')
    list_filter = ('date', 'active')
    search_fields = ('name', 'post')


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
