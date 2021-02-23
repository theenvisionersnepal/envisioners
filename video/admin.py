from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'youtube_link', 'video_code', 'date')


admin.site.register(Video, VideoAdmin)