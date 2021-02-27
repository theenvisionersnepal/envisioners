"""theenvisionersnepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, photos
from video.views import video
from member.views import members, about_us
from explanation.views import explanation_view
from blog.views import blog, blog_detail, category_detail
urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),

    path('social-posts/', photos, name='photos'),
    path('blogs/', blog, name='blog'),
    path('videos/', video, name='video'),
    path('members/', members, name='member'),
    path('about-us/', about_us, name='about-us'),
    path('explanation/', explanation_view, name='explanation'),
    path('<slug:slug>/', category_detail, name='category_detail'),

    path('<slug:category_slug>/<slug:slug>', blog_detail, name='blog_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
