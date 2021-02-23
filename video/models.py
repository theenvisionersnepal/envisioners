from django.db import models


class Video(models.Model):
    video_title = models.CharField(max_length=256)
    youtube_link = models.CharField(max_length=256)
    video_code = models.CharField(max_length=256)
    date = models.DateField()
