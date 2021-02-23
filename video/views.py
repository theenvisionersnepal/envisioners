from django.shortcuts import render
from .models import Video


def video(request):
    latest_videos = Video.objects.filter().order_by('-date')[0:1]
    videos = Video.objects.all().order_by('-date')
    context = {
        'latest_videos': latest_videos,
        'videos': videos
    }
    return render(request, 'video.html', context)
