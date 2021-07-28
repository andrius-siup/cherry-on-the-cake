from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    content = models.CharField(max_length=100000, null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.title
