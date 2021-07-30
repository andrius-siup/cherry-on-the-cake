from django.db import models
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=True, blank=True)
    content = models.CharField(max_length=100000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.title
