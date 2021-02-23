from django.db import models


class Member(models.Model):
    Name = models.CharField(max_length=256)
    Skills = models.CharField(max_length=256, null=True, blank=True)
    Email = models.CharField(max_length=256, null=True, blank=True)
    Phone = models.CharField(max_length=256, null=True, blank=True)
    Facebook_link = models.CharField(max_length=2048, null=True, blank=True)
    Instagram_link = models.CharField(max_length=2048, null=True, blank=True)
    Image_url = models.CharField(max_length=2048, null=True, blank=True)
    Co_founder = models.BooleanField(default=False)
