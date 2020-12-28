from django.db import models


class Books(models.Model):
    # Example model only
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    post = models.TextField(max_length=250, blank=True)
    # genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # isbn = models.CharField(max_length=100)
    # count = models.IntegerField(null=True, default=0)
