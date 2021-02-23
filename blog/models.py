from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=256)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    category = models.ForeignKey(Category, related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    date = models.DateTimeField()
    author = models.CharField(max_length=256)
    image_url = models.CharField(max_length=2048)
    post = models.TextField()
    Image_Credit = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)
