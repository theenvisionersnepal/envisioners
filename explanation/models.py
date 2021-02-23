from django.db import models
from tinymce import models as Tinymcemodels


class Explanation(models.Model):
    title = models.CharField(max_length=256)
    content = Tinymcemodels.HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
